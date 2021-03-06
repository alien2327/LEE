# 기본예제로 주어진 cartpole은 observation의 결과와 관계 없이 다음 행동을 랜덤으로 취했기 때문에,
# 움직임이 불안정하고, pole을 세우려고 노력하는 모습이 보이지 않았다.
# 때문에 첫번째 응용으로써 observation의 결과가 다음 action에 영향을 주게끔 코드를 수정해보았다.

"""
import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
"""

import gym

env = gym.make('CartPole-v0')
total_reward_sum = [0] * 20
for i_episode in range(20):
    observation = env.reset()
    total_reward = 0
    # total_reward를 통해 처음 보상의 시작값을 설정
    
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        sum_obs = observation[0] + observation[1] + observation[2] + observation[3]
        if sum_obs > 0:
            action = 1
        else:
            action = 0
        # observation결과 값에 따라 다음 행동을 할지 결정.
        # sum_obs, 즉 관측한 결과 값을 모두 더한 수치에 따라 다음 행동의 진행 여부를 결정
        
        observation, reward, done, info = env.step(action)
        total_reward += 1
        # 행동이 진행되면 1을 더함
        
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("total reward is"),
            print(total_reward)
            total_reward_sum[i_episode] = total_reward
            if i_episode == 19:
                print("all total reward is"),
                print(total_reward_sum)
            break
        # 결과와 보상 수치를 출력
        
        if t == 99:
            print("Episode finished after {} timesteps".format(t+1))
            print("total reward is"),
            print(total_reward)
            total_reward_sum[i_episode] = total_reward
            if i_episode == 19:
                print("all total reward is"),
                print(total_reward_sum)
env.close()
