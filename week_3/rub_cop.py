import math
price = float(input())
cops = math.ceil(price * 100)
print(cops // 100, cops % 100)
