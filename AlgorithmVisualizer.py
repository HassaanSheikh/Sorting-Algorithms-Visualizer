import sys
from matplotlib import animation
import numpy as np 
import scipy as sy 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import random
import time

sys.path.append('C:/coding stuff/SortingVisualizer/Algorithms')

from bubbleSort import *

class TrackedArray():

    def __init__(self, list):
        self.list = np.copy(list)
        self.reset()
    
    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    def __getitem__(self, key):
        self.track(key, "get")
        return self.list.__getitem__(key)
    
    def __setitem__(self, key, value):
        self.list.__setitem__(key,value)
        self.track(key, "set")
    
    def __len__(self):
        return self.list.__len__()
    
    def track(self, key, access_type):
        self.indices.append(key)
        self.values.append(self.list[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.list))
    
    def GetActivity(self, idx=None):
        if isinstance(idx, type(None)):
            return [(i, op) for (i, op) in zip(self.indices, self.access_type)]
        else:
            return (self.indices[idx], self.access_type[idx])

plt.rcParams['figure.figsize'] = (12,8)
plt.rcParams['font.size'] = 16

FPS = 120

list = []
for i in range(0,50):
    list.append(random.randrange(10,500))

list = TrackedArray(list)

## First algorithm - Shell Sort



t = time.perf_counter()

algorithm = "ShellSort"
bubbleSort(list)

fig, ax = plt.subplots()
container = ax.bar(np.arange(0,len(list),1), list, align='edge', width=0.8)
ax.set_xlim([0,len(list)])
ax.set(xlabel="Index", ylabel="Value", title=algorithm)
txt = ax.text(0,488, "")


def update(frame):
    txt.set_text(f" Accesses = {frame}")
    for (rectangle, height) in zip(container.patches, list.full_copies[frame]):
        rectangle.set_height(height)
        rectangle.set_color("g")
    idx, op = list.GetActivity(frame)
    if op == "get":
        container.patches[idx].set_color("m")
    elif op == "set":
        container.patches[idx].set_color("r")
    
    return(*container, txt)

vis = FuncAnimation(fig, update, frames = range(len(list.full_copies)), 
blit = True, interval=1./FPS, repeat = False)

t2 = time.perf_counter() - t
print(t2)
plt.show()
