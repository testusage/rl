import gymnasium as gym
import time

env = gym.make("FrozenLake-v1" , render_mode="human")
env.reset()
env.render()

print(env.observation_space)
print(env.action_space)
print(env.P[3][1])

env.reset()

#1
# num_steps = 10
# ret=0
# for t in range(num_steps):
#     rnd_action=env.action_space.sample()
#     (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
#     ret=ret+reward
#     env.render()
#     time.sleep(1)
#     if done:
#         break
#     print('Return of this episode: ',ret)

# #2
# num_eps=5
# for n in range(num_eps):
#     env.reset()
#     num_steps=10
#     ret=10
#     for t in range(num_eps):
#         rnd_action=env.action_space.sample()
#         (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
#         ret=ret+reward
#         env.render()
#         time.sleep(1)
#         if done:
#             break
#     print("return of episode",n,'is',ret)

#3
# num_eps=10
# for i in range(num_eps):
#     ret=0
#     pol=[]
#     env.reset()
#     num_steps=5
#     for n in range(num_steps):
#         rnd_action=env.action_space.sample()
#         pol.append(rnd_action)
#         (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
#         ret=ret+reward
#         env.render()
#         time.sleep(2)
#         if done:
#             break
#     print('Return of episode {0} is {1}'.format(i+1,ret))
#     print("Policy of episode {0} is {1}".format(i+1,pol))

#4
num_eps=10
for i in range(num_eps):
    ret=0
    pol_words=[]
    pol_ints= []
    actions={0:0,1:0,2:0,3:0}
    env.reset()
    num_steps=5
    for n in range(num_steps):
        rnd_action=env.action_space.sample()
        pol_ints.append(rnd_action)
        if rnd_action == 0:
            pol_words.append('left')
        elif rnd_action == 1:
            pol_words.append('down')
        elif rnd_action == 2:
            pol_words.append('right')
        else:
            pol_words.append('up')
        (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
        ret=ret+reward
        env.render()
        time.sleep(1)
        if done:
            break
    print('Return of episode {0} is {1}'.format(i+1,ret))
    print("Policy of episode {0} is {1}".format(i+1,pol_words))
    print('***************')
    for a in range(len(pol_ints)):
        if pol_ints[a] == 0:
            actions[0] =actions[0]+1
        elif pol_ints[a] == 1:
            actions[1] =actions[1]+1
        elif pol_ints[a] == 2:
            actions[2] =actions[2]+1
        else:
            actions[3] =actions[3]+1
    print('Action count of this episode',actions)
#------------------------------------------------------------------------------------------------------------------------

# import gymnasium as gym
# import time

# env = gym.make("CartPole-v1",render_mode="human")
# env.reset()
# env.render()

# #state and action space
# print(env.observation_space)
# print(env.action_space)

# # 1 episode with 10 steps
# num_steps = 10
# ret = 0
# env.reset()
# for i in range(num_steps):
#     action = env.action_space.sample()
#     s_ , reward , tp , done , _ =env.step(action)
#     env.render()
#     time.sleep(1)
#     ret += reward
#     if done : 
#         break
# print("Return : " , ret)

# # 10 episodes
# num_eps = 10
# for t in range(num_eps):
#     num_steps = 10
#     ret = 0
#     env.reset()
#     for i in range(num_steps):
#         action = env.action_space.sample()
#         s_ , reward , tp , done , _ =env.step(action)
#         env.render()
#         time.sleep(1)
#         ret += reward
#         if done:
#             break
#     print("return of episode {0} is {1} ".format(t,ret))

# # Save the returns in a dictionary
# num_epsds =10
# ret_dict = {}
# for i in range(num_epsds):
#     num_steps=20
#     ret = 0
#     env.reset()
#     for t in range(num_steps):
#         action = env.action_space.sample()
#         s_,reward,tp,done,_= env.step(action)
#         env.render()
#         time.sleep(1)
#         ret =ret+reward
#         if done:
#             break
#     ret_dict[i] = ret
# print("the return is ",ret_dict)