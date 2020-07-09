# UARA-DRL

I have been learning on how to use deep reinforcement learning (DRL) to solve problems in wireless communications and networking. The model I used in this repository is based on deep-Q-network (DQN) and DDQN. For more details on DQN and DDQN, I suggest you to read the paper V. Minh et al., "Human-level control through deep reinforcement learning", Nature, vol. 518, pp. 529–533, 2015, which can be found in https://www.nature.com/articles/nature14236.

Specifically, this project is an implementation of the paper N. Zhao, Y. Liang, D. Niyato, Y. Pei, M. Wu and Y. Jiang, "Deep reinforcement learning for user association and resource allocation in heterogeneous cellular networks," IEEE Transactions on Wireless Communications, vol. 18, no. 11, pp. 5141-5152, Nov. 2019. Please cite this paper if you learn about their system models, problem formulation, or algorithms.

Prerequisite: Python 3.7, Pytorch.

Initially, this implementation is develped based on the classical DRL tutorial for the CartPole-v0 task, which can be found in https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html. It will help a beginner to learn about how to implement deep reinforcement learning using Pytorch. For the multi-agent part, I mainly consulted the paper Foerster et al., "Learning to communicate with deep multi-agent reinforcement learning", NIPS 2016. The Pytorch implementation of this paper can be found in https://github.com/minqi/learning-to-communicate-pytorch.
