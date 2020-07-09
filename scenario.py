# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:51:49 2020

@author: liangyu

Create the network simulation scenario
"""

import numpy as np
from numpy import pi
from random import random, uniform, choice

class BS:  # Define the base station
    
    def __init__(self, sce, BS_index, BS_type, BS_Loc, BS_Radius):
        self.sce = sce
        self.id = BS_index
        self.BStype = BS_type
        self.BS_Loc = BS_Loc
        self.BS_Radius = BS_Radius
        
    def reset(self):  # Reset the channel status
        self.Ch_State = np.zeros(self.sce.nChannel)    
        
    def Get_Location(self):
        return self.BS_Loc
    
    def Transmit_Power_dBm(self):  # Calculate the transmit power of a BS
        if self.BStype == "MBS":
            Tx_Power_dBm = 40   
        elif self.BStype == "PBS":
            Tx_Power_dBm = 30 
        elif self.BStype == "FBS":
            Tx_Power_dBm = 20 
        return Tx_Power_dBm  # Transmit power in dBm, no consideration of power allocation now
    
    def Receive_Power(self, d):  # Calculate the received power by transmit power and path loss of a certain BS
        Tx_Power_dBm = self.Transmit_Power_dBm()
        if self.BStype == "MBS" or self.BStype == "PBS":
            loss = 34 + 40 * np.log10(d)
        elif self.BStype == "FBS":
            loss = 37 + 30 * np.log10(d)  
        if d <= self.BS_Radius:
            Rx_power_dBm = Tx_Power_dBm - loss  # Received power in dBm
            Rx_power = 10**(Rx_power_dBm/10)  # Received power in mW
        else:
            Rx_power = 0.0
        return Rx_power        
        
        
class Scenario:  # Define the network scenario
    
    def __init__(self, sce):  # Initialize the scenario we simulate
        self.sce = sce
        self.BaseStations = self.BS_Init()        
        
    def reset(self):   # Reset the scenario we simulate
        for i in range(len(self.BaseStations)):
            self.BaseStations[i].reset()
            
    def BS_Number(self):
        nBS = self.sce.nMBS + self.sce.nPBS + self.sce.nFBS  # The number of base stations
        return nBS
    
    def BS_Location(self):
        Loc_MBS = np.zeros((self.sce.nMBS,2))  # Initialize the locations of BSs
        Loc_PBS = np.zeros((self.sce.nPBS,2))
        Loc_FBS = np.zeros((self.sce.nFBS,2)) 
        
        for i in range(self.sce.nMBS):
            Loc_MBS[i,0] = 500 + 900*i  # x-coordinate
            Loc_MBS[i,1] = 500  # y-coordinate
        
        for i in range(self.sce.nPBS):
            Loc_PBS[i,0] = Loc_MBS[int(i/4),0] + 250*np.cos(pi/2*(i%4))
            Loc_PBS[i,1] = Loc_MBS[int(i/4),1] + 250*np.sin(pi/2*(i%4))
            
        for i in range(self.sce.nFBS):
            LocM = choice(Loc_MBS)
            r = self.sce.rMBS*random()
            theta = uniform(-pi,pi)
            Loc_FBS[i,0] = LocM[0] + r*np.cos(theta)
            Loc_FBS[i,1] = LocM[1] + r*np.sin(theta)

        return Loc_MBS, Loc_PBS, Loc_FBS
    
    def BS_Init(self):   # Initialize all the base stations 
        BaseStations = []  # The vector of base stations
        Loc_MBS, Loc_PBS, Loc_FBS = self.BS_Location()
        
        for i in range(self.sce.nMBS):  # Initialize the MBSs
            BS_index = i
            BS_type = "MBS"
            BS_Loc = Loc_MBS[i]
            BS_Radius = self.sce.rMBS            
            BaseStations.append(BS(self.sce, BS_index, BS_type, BS_Loc, BS_Radius))
            
        for i in range(self.sce.nPBS):
            BS_index = self.sce.nMBS + i
            BS_type = "PBS"
            BS_Loc = Loc_PBS[i]
            BS_Radius = self.sce.rPBS
            BaseStations.append(BS(self.sce, BS_index, BS_type, BS_Loc, BS_Radius))
            
        for i in range(self.sce.nFBS):
            BS_index = self.sce.nMBS + self.sce.nPBS + i
            BS_type = "FBS"
            BS_Loc = Loc_FBS[i]
            BS_Radius = self.sce.rFBS
            BaseStations.append(BS(self.sce, BS_index, BS_type, BS_Loc, BS_Radius))
        return BaseStations
            
    def Get_BaseStations(self):
        return self.BaseStations


        
            
    

