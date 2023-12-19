def factorial(n, f=lambda x: x):
    n = f(n)

    if n <= 2:
        return n

    return n * factorial(n - 1)


def f(x):
    if x % 2:
        return x ** 2
    return x ** 2 + 1


print([factorial(n) for n in range(10)])
