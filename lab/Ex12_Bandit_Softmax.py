# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:20:14 2023

@author: Admin
"""
#import necessary libraries
import gym

import gym_bandits 

import numpy as np

#create the environment
env = gym.make("BanditTwoArmedHighLowFixed-v0")
#print(env.action_space.n)

print(env.p_dist) 

env.reset()  

#define the softmax function to choose an arm in each round
def softmax(T):
    denom = sum([np.exp(i/T) for i in Q])
    probs = [np.exp(i/T)/denom for i in Q]
    arm = np.random.choice(env.action_space.n, p=probs)
    return arm 



#initialize the count, sum_rewards and Q of all the arms
count = np.zeros(2)
sum_rewards = np.zeros(2)
Q = np.zeros(2) 

#initialize the parameters
num_rounds = 100
T = 50  

#generate the rounds
for i in range(num_rounds):
    arm = softmax(T)
    next_state, reward, done, info = env.step(arm)
    count[arm] += 1
    sum_rewards[arm]+=reward
    Q[arm] = sum_rewards[arm]/count[arm]
    T = T*0.99

#print the average reward of all the arms
print(Q)

#print the optimal arm
print('The optimal arm is arm {}'.format(np.argmax(Q)+1))
