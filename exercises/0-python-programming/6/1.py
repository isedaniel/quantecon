# print bool type methods
methods = [i for i in dir(True) if callable(eval(f"True.{i}"))]
print(methods)
