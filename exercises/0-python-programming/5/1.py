def vproduct(x, y):
    """Given two vectors x and y, gets the inner product"""
    total = 0
    for i, j in zip(x, y):
        total += i*j
    return total


x = (1, 2, 3)
y = (2, 3, 4)
print(f"vproduct: { vproduct(x, y) }")


def iseven(n):
    """return True if n is even"""
    return n % 2 == 0


even = len([n for n in range(100) if iseven(n)])
print(f"even: { even }")


def evenpairs(pairs):
    total = 0

    for x, y in pairs:
        if iseven(x) and iseven(y):
            total += 1
    return total


pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
print(f"even pairs: { evenpairs(pairs) }")
