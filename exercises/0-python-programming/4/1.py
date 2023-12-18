
def factorial(n, f=lambda x: x):
    n = f(n)

    if n <= 2:
        return n

    return n * factorial(n - 1)


def f(x):
    if x % 2:  # if x is odd
        return x ** 2
    return x ** 2 + 1


# some test with n numbers
n = 5
for i in range(n+1):
    print(f"{ i }: { factorial(i) }")

print()  # new line

for i in range(n+1):
    print(f"{ f(i) }: { factorial(i, f) }")
