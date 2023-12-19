# again but with comprenhension instead of functions
xtuple = (1, 2, 3)
ytuple = (2, 3, 4)

s = sum(x * y for x, y in zip(xtuple, ytuple))
test = "Solved" if s == 20 else f"Expected 20 but got { s }"
print(f"inner product: { test }")


s = sum(1 for x in range(100) if x % 2 == 0)
test = "Solved" if s == 50 else f"Expected 50 but got { s }"
print(f"even numbers: { test }")


pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
s = sum(1 for x, y in pairs if x % 2 == 0 and y % 2 == 0)
test = "Solved" if s == 2 else f"Expected 2 but got { s }"
print(f"pairs: { test }")
