# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:26:03 2023

@author: Admin
"""

#import necessary libraries
import gym
import gym_bandits
import numpy as np

#create the environment
env = gym.make("BanditTwoArmedHighLowFixed-v0")
print(env.action_space.n)
print(env.p_dist)
env.reset()

#initialize the arrays and the parameters
count = np.zeros(2)
sum_rewards = np.zeros(2)
Q = np.zeros(2)

alpha=np.ones(2)
beta=np.ones(2)
num_rounds = 100


#define the exploration strategy – Thompson sampling
def thompson_sampling(alpha,beta):
    samples = [np.random.beta(alpha[i]+1,beta[i]+1) for i in range(2)]
    return np.argmax(samples)

#generate the rounds
for i in range(num_rounds):
    arm = thompson_sampling(alpha,beta)
    next_state, reward, done, info = env.step(arm)
    count[arm] += 1
    sum_rewards[arm]+=reward
    Q[arm] = sum_rewards[arm]/count[arm]
    
    if reward==1:
        alpha[arm] = alpha[arm] + 1
    else:
        beta[arm] = beta[arm] + 1

print(Q)
print('The optimal arm is arm {}'.format(np.argmax(Q)+1))
