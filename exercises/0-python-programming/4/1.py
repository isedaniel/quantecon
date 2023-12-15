# %matplotlib inline
# import numpy as np
#import matplotlib.pyplot as plt

#plt.rcParams['figure.figsize'] = (10, 6)


def factorial(n, f=lambda x: x):
    if n <= 2:
        return n

    return f(n) * factorial(f(n) - 1, f)


n = 5
for i in range(n+1):
    print(f"{i}: {factorial(i)}")


for i in range(n+1):
    print(f"{i}: {factorial(i, lambda x: x + 1)}")
