import matplotlib.pyplot as plt
import time
from controller import *
import random
from timeit import default_timer as timer
import numpy as np

newPid = PID(0.3, 0.01, 0.15, 0.05)

# vals = [0.1, 0.2, 0.1, 0.3, 0.5, 0.4, 0.3, 0.2, 0.7, 0.8, 1, 2, 4, 0.34, 0.67, 0.876]
# sorted_vals = sorted(vals)

time = np.arange(0, 10, 0.1)

amplitude = np.sin(time)

dt = 0.05
ts = np.arange(0, 75, dt)

for i in amplitude:
    angle = i
    print(angle)
    error = angle - dAngle
    newPid.call(error, 2)

def fix(array):
    array.extend(np.full(len(ts) - len(array), array[0]))

fix(error_plot)
fix(p_plot)
fix(i_plot)
fix(d_plot)

fig, ax = plt.subplots()

ax.plot(ts, error_plot, label = 'Error')
ax.plot(ts, p_plot, label = 'P')
ax.plot(ts, i_plot, label = 'I')
ax.plot(ts, d_plot, label = 'D')

plt.ylabel('val')
plt.xlabel('time')

plt.title('PID Sim')
plt.show()

