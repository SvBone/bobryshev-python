a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D == 0:
    x = -b / (2 * a)
    print(x)
elif D > 0:
    x_1 = (-b - D ** 0.5) / (2 * a)
    x_2 = (-b + D ** 0.5) / (2 * a)
    if x_1 > x_2:
        x_1, x_2 = x_2, x_1
    print(x_1, x_2)
