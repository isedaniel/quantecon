import numpy as np
import matplotlib.pyplot as plt

a = 0.9
T = 200
X = np.empty(T + 1)
X[0] = 0

for t in range(T):
    abs_x = - X[t] if X[t] < 0 else X[t]
    X[t+1] = a * abs_x + np.random.randn()

plt.plot(X, label=f'$\\alpha = {a}$')
plt.legend()
plt.show()
