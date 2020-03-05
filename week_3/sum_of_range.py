n = float(input()) + 1
result = 0
counter = 1
eps = 10 ** (-6)
while n - counter > eps:
    result += 1 / (counter ** 2)
    counter += 1
print(result)
