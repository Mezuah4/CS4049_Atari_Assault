# For deep neural networks
# import tensorflow.compat.v1 as tf
import tf_slim as slim

# For data representation
import numpy as np
import random

# For handling files
import os

# For plotting graphs
import matplotlib
import matplotlib.pyplot as plt

# OpenAI Gym
import gym
# I have installed pyglet-1.5.11 for it work with BigSur


all_env = list(gym.envs.registry.all())
for e in all_env:
    if "Assault" in str(e):
        print(e)

env = gym.make("Assault-v0")

env.reset()
for i in range(20):
    print(env.step())