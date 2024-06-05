# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-

#import necessary libraries
import gym
import gym_bandits 
import numpy as np

#create the envt and print the no. of actions, prob distbn of the arms
env = gym.make("BanditTwoArmedHighLowFixed-v0")
print(env.action_space.n)
print(env.p_dist)
env.reset()

#initialize count, sum-of-rewards and average reward of all arms to zero
count = np.zeros(2)
sum_rewards = np.zeros(2)
Q = np.zeros(2) 


#define a function for epsilon-greedy policy
def epsilon_greedy(epsilon):
 
 if np.random.uniform(0,1) < epsilon:
     return env.action_space.sample()
 else:
     return np.argmax(Q)

#initialize the parameters
num_rounds = 100

#generate several rounds
for i in range(num_rounds):
    arm = epsilon_greedy(epsilon=0.5)
    next_state, reward, done, info = env.step(arm)
    count[arm] += 1
    sum_rewards[arm]+=reward
    Q[arm] = sum_rewards[arm]/count[arm]

#print the average reward of both arms
print(Q)
#print the optimal arm
print('The optimal arm is arm {}'.format(np.argmax(Q)+1))