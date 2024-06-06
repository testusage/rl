
#TD PREDICTION
import gymnasium as gym
import pandas as pd

#create the envt 
env = gym.make("FrozenLake-v1", render_mode = "human")
env.reset()

env.render() 

def random_policy():
    return env.action_space.sample()

V = {}
for s in range(env.observation_space.n):
    V[s] = 0.0 


alpha = 0.85
gamma = 0.90

num_eps = 50
num_steps = 10

for i in range(num_eps): 
    s = env.reset()
    s = s[0]
    for t in range(num_steps): 
        a = random_policy()
        s_, r, done, _, _ = env.step(a) 
        
                    
        V[s] += alpha * (r + gamma * V[s_] - V[s])             
        s = s_
        if done: 
           break

df = pd.DataFrame(list(V.items()), columns = ['state', 'value'])
print(df) 

#Sample Output after 5000 episodes

#    state     value
#0       0  0.000409
#1       1  0.000005
#2       2  0.007377
#3       3  0.000351
#4       4  0.003835
#5       5  0.000000
#6       6  0.004941
#7       7  0.000000
#8       8  0.000642
#9       9  0.014566
#10     10  0.112160
#11     11  0.000000
#12     12  0.000000
#13     13  0.059375
#14     14  0.529872
#15     15  0.000000
