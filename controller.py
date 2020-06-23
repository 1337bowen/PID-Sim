import time
import warnings

import numpy as np
import random
import math


g = 9.8 # m/s
mass = 3442

Fg = mass * g

# print(f'Weight = {Fg:.2f} N')

max_thrust = 44230
Isp = 280
mdot = max_thrust / (Isp * g)

# print(f'TWR = {max_thrust / Fg:.2f}')
# print(f'mdot = {mdot:.2f} kg')


def thrust(throttle):
  return max_thrust * throttle

dAngle = 0

error_plot = []
p_plot = []
i_plot = []
d_plot = []

err_plot = []
errSum_plot = []
dt_plot = []

class PID:

    def __init__(self, Kp, Ki, Kd, dt):

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt

        self.error_sum = 0
        self.last_error = 0

    def call(self, error, thresh):
        error_plot.append(error)
        p = self.Kp * error
        p_plot.append(p)
        i = self.Ki * self.error_sum
        i_plot.append(i)
        d = self.Kd * (error - self.last_error) / self.dt
        d_plot.append(d)

        self.thresh = thresh

        is_stable = abs(error) < self.thresh
        
        if not is_stable:
            print('not stable')
        
        self.last_error = error
        err_plot.append(error)


        tvcPID = p + i + d
        rAngle = dAngle + tvcPID
        print("pid = " + str(tvcPID))
        print("rAngle = " + str(rAngle))
        return p + i + d

    




