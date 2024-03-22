# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:11:24 2023

@author: HP
"""
#Q1create and render the environment
import gymnasium as gym 
import time

#from gymnasium.wrappers.monitoring import video_recorder
#from gymnasium.wrappers.monitoring.video_recorder import VideoRecorder 

env = gym.make("CartPole-v1", render_mode = "human")

env.reset()

env.render()

#Q2 explore state space and action space
#print state space which is continuous
print(env.observation_space)

#print action space
print(env.action_space)


env.reset()
#implement with a random policy

#Q3.generate one episode with 10 time steps and print its return using a random policy
num_steps=10
ret = 0
env.reset()
for t in range(num_steps):
    action = env.action_space.sample()
    s_,reward,tp,done,_= env.step(action)
    env.render()
    time.sleep(1)
    ret =ret+reward
    if done:
        break
print("return = ",ret)

#Q4.generate 10 episodes using a random policy and print n returns
num_epsds =10
for i in range(num_epsds):
    num_steps=20
    ret = 0
    env.reset()
    for t in range(num_steps):
        action = env.action_space.sample()
        s_,reward,tp,done,_= env.step(action)
        env.render()
        time.sleep(1)
        ret =ret+reward
        if done:
            break
    print("return of episode {0} is {1} ".format(i,ret))

#Q5. Save the returns in a dictionary
num_epsds =10
ret_dict = {}
for i in range(num_epsds):
    num_steps=20
    ret = 0
    env.reset()
    for t in range(num_steps):
        action = env.action_space.sample()
        s_,reward,tp,done,_= env.step(action)
        env.render()
        time.sleep(1)
        ret =ret+reward
        if done:
            break
    ret_dict[i] = ret
print("the return is ",ret_dict)
    

    
