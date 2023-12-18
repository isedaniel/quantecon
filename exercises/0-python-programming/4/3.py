from numpy.random import uniform


# pay one dollar if a head occurs k or more times consecutively
def consecutive_pay(k):
    total = 0
    heads = 0

    for i in range(10):
        u = uniform()
        heads = heads + 1 if u < 0.5 else 0
        print(f"i: {i} heads: {heads}")
        if heads == k:
            total = 1
            break

    return total


# pay one dollar if a head occurs k or more times 
def pay(k):
    heads = 0

    for i in range(10):
        u = uniform()
        heads = heads + (1 if u < 0.5 else 0)
        print(f"i: {i} heads: {heads}")

    return int(heads >= k)  # return 1 dollar if true


print(f"pay: {pay(3)}")

print(f"pay: {consecutive_pay(3)}")
