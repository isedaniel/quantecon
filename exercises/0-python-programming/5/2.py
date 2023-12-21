def p(x, coeff):
    total = 0
    for i, c in enumerate(coeff):
        total += c * x ** i
        print(f"{c * x ** i} = {c} * {x} ** {i}")
        print(f"total = {total}")
    return total


coeff = (1, 2, 3)
x = 2
print(p(x, coeff))
