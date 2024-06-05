# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:55:30 2023

@author: HP
"""


#Implementation of Every-visit Monte Carlo Prediction for Blackjack environment.

#import libraries
import pandas as pd
from collections import defaultdict
import gymnasium as gym

#create teh environment
env=gym.make('Blackjack-v1',render_mode='human')
env.reset()
env.render()

#define the input policy
def policy(state):
    return 0 if state[0]>19 else 1

#print the policy of the initial state
state = env.reset()
state=state[0]
print(state)
print(policy(state))

$generate one episode from the initial state using the policy defined
num_timesteps = 100
def generate_episode(policy):
    episode = []
    state = env.reset()
    state=state[0]
    for t in range(num_timesteps):
        action = policy(state)
        next_state, reward, done, info,trans_prob = env.step(action)
        episode.append((state, action, reward))
        #print("Done is",done)
        if done:
            break
        state=next_state
    return episode
print(generate_episode(policy)) 


#using every-visit MC find V(s)
#initialize the dictionary for total_return and N
total_return = defaultdict(float)
N = defaultdict(int) 

num_iterations = 10
for i in range(num_iterations):
    episode = generate_episode(policy)
    states, actions, rewards = zip(*episode)
    for t, state in enumerate(states):
        R = (sum(rewards[t:]))
        total_return[state] = total_return[state] + R
        N[state] = N[state] + 1
        
print(total_return[state])
print(N[state])
 
#convert the dictionaries to a data frame       
total_return = pd.DataFrame(total_return.items(),columns=['state', 'total_return'])
N = pd.DataFrame(N.items(),columns=['state', 'N'])
df = pd.merge(total_return, N, on="state")
print(df.head(10))
df['value'] = df['total_return']/df['N']
print(df.head(10))
print(df.shape)

#evaluate the value of some of the states
print(df[df['state']==(20,2,False)]['value'].values)
print(df[df['state']==(5,8,False)]['value'].values)


env.close()