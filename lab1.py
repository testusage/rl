import gymnasium as gym
import time

env=gym.make('FrozenLake-v1',render_mode='human')
env.reset()
env.render()

print(env.observation_space)

print(env.action_space)

print(env.P[3][1])

(next_state,trans_prob,reward,done,_)=env.step(1)
env.render()

env.reset()
rnd_action = env.action_space.sample()
(next_state,trans_prob,reward,done,_)=env.step(rnd_action)
env.render()




env.reset()
num_steps = 10
ret=0
for t in range(num_steps):
    rnd_action=env.action_space.sample()
    (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
    ret=ret+reward
    env.render()
    time.sleep(1)
    if done:
        break
    print('Return of this episode: ',ret)
    

num_eps=5
for n in range(num_eps):
    env.reset()
    num_steps=10
    ret=10
    for t in range(num_eps):
        rnd_action=env.action_space.sample()
        (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
        ret=ret+reward
        env.render()
        time.sleep(1)
        if done:
            break
    print("return of episode",n,'is',ret)

num_eps=10
for i in range(num_eps):
    ret=0
    env.reset()
    num_steps=20
    for n in range(num_steps):
        rnd_action=env.action_space.sample()
        (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
        ret=ret+reward
        env.render()
        time.sleep(1)
        if done:
            break
    print('Return of episode {0} is {1}'.format(i+1,ret))


num_eps=10
for i in range(num_eps):
    ret=0
    pol=[]
    env.reset()
    num_steps=20
    for n in range(num_steps):
        rnd_action=env.action_space.sample()
        pol.append(rnd_action)
        (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
        ret=ret+reward
        env.render()
        time.sleep(2)
        if done:
            break
    print('Return of episode {0} is {1}'.format(i+1,ret))
    print("Policy of episode {0} is {1}".format(i+1,pol))


num_eps=10
for i in range(num_eps):
    ret=0
    pol=[]
    env.reset()
    num_steps=20
    for n in range(num_steps):
        rnd_action=env.action_space.sample()
        if rnd_action == 0:
            pol.append('left')
        elif rnd_action == 1:
            pol.append('down')
        elif rnd_action == 2:
            pol.append('right')
        else:
            pol.append('up')
        (next_state,trans_prob,reward,done,_)=env.step(rnd_action)
        ret=ret+reward
        env.render()
        time.sleep(2)
        if done:
            break
    print('Return of episode {0} is {1}'.format(i+1,ret))
    print("Policy of episode {0} is {1}".format(i+1,pol))

num_eps=10
for i in range(num_eps):
    ret=0
    pol_words=[]
    pol_ints= []
    actions={0:0,1:0,2:0,3:0}
    env.reset()
    num_steps=20
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
    print("Policy of episode {0} is {1}".format(i+1,pol_ints))

num_eps=10
for i in range(num_eps):
    ret=0
    pol_words=[]
    pol_ints= []
    actions={0:0,1:0,2:0,3:0}
    env.reset()
    num_steps=20
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


num_eps=10
for i in range(num_eps):
    ret=0
    pol_words=[]
    pol_ints= []
    actions={0:0,1:0,2:0,3:0}
    env.reset()
    num_steps=20
    for n in range(num_steps):
        rnd_action=env.action_space.sample()
        actions[rnd_action] += 1
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
    print('Action count of this episode',actions)