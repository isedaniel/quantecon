# %matplotlib inline
# import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 6)


def f(x, y, a=1, b=1):
    return a*x + b


print(f(y=1, x=3, a=2))
print(f(2, 2))
