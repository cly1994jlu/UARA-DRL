# UARA-DRL

Learned to use deep reinforcement learning (DRL) to solve problems in wireless communications and networking. The model I use is based on deep-Q-network (DQN) and DDQN. For more details on DQN and DDQN, I suggest to consult the paper V. Minh et al., "Human-level control through deep reinforcement learning", Nature, vol. 518, pp. 529–533, 2015, which can be found in https://www.nature.com/articles/nature14236.

This project is an implementation of the paper N. Zhao, Y. Liang, D. Niyato, Y. Pei, M. Wu and Y. Jiang, "Deep reinforcement learning for user association and resource allocation in heterogeneous cellular networks," IEEE Transactions on Wireless Communications, vol. 18, no. 11, pp. 5141-5152, Nov. 2019. Please cite this paper for system models, and problem formulation if you learn from that.

Prerequisite:

Python 3.7, Pytorch

The implementation is based on the classical DRL for CartPole-v0 task. The tutorial can be found in https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html. It will help a beginner to learn about reinforcement learning implementation. For the multi-agent part, I mainly considered the paper Foerster et al., "Learning to Communicate with Deep Multi-Agent Reinforcement Learning", NIPS 2016. The Pytorch implementation can be found in https://github.com/minqi/learning-to-communicate-pytorch.
