from functools import reduce

res = reduce(lambda a, b: a * b, [el for el in range(100, 1001) if el % 2 == 0])

print(res)