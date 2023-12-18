# %matplotlib inline
# import numpy as np
# import matplotlib.pyplot as plt

# plt.rcParams['figure.figsize'] = (10, 6)


def factorial(n, f=lambda x: x):
    n = f(n)

    if n <= 2:
        return n

    return n * factorial(n - 1)


def f(x):
    if x % 2:  # if x is odd
        return x ** 2
    return x ** 2 + 1


n = 5
for i in range(n+1):
    print(f"{i}: {factorial(i)}")

print()

for i in range(n+1):
    print(f"{f(i)}: {factorial(i, f)}")
