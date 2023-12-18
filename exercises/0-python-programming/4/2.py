from numpy.random import uniform


# binomial random variable: represents number of successes in n trials with
# probability p
def brv(n, p):
    successes = 0
    for _ in range(n):
        if uniform() < p:
            successes += 1
    return successes


print(brv(10, 0.5))
