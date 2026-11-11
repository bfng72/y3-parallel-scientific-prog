import numpy as np
from matplotlib import pyplot as plt


x_0 = 500
v_0 = 0

g = 9.81

time_step = 0.01

alpha = 0.8

bounces = 3

x = x_0
v = v_0
t = 0

t_array = [0]
x_array = [x]
v_array = [v]

def fall(x, v, t):
    while True:
        v += -g * time_step
        x += v * time_step
        t += time_step
        
        x_array.append(x)
        t_array.append(t)
        v_array.append(v)

        if x <= 0:
            break
    return x, v, t

def bounce(x, v, t):
    x=0
    v = -alpha * v
    t += time_step

    x_array.append(x)
    t_array.append(t)
    v_array.append(v)

    return x, v, t

for i in range(bounces):
    x, v, t = fall(x, v, t)
    x, v, t = bounce(x, v, t)

fall(x, v, t)


plt.plot(t_array, x_array)
plt.plot(t_array, v_array)
plt.legend(["x", "v"])
plt.xlabel("time (s)")
plt.show()
    