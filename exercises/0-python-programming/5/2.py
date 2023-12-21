def p(x, coeff):
    return sum(a * x**i for i, a in enumerate(coeff))


coeff = (2, 4)
x = 1
print(p(x, coeff))
