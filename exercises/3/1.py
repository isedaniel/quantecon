import numpy as np
import matplotlib.pyplot as plt

a = 0.9
T = 200
x = np.empty(T+1)
x[0] = 0

for t in range(T):
    x[t+1] = a*x[t] + np.random.randn()

plt.plot(x)
plt.show()
