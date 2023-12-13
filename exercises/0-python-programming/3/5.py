# aprox of Pi using monte carlo
import numpy as np

samples = 1_000_000
x = np.random.uniform(-1, 1, samples)
y = np.random.uniform(-1, 1, samples)

# points in circle
p_c = 0
for i in range(samples):
    # calc distance from origin
    d = x[i] ** 2 + y[i] ** 2

    if d <= 1:
        p_c += 1

pi = 4*p_c / samples
print(pi)
