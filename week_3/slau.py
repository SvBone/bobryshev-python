a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
flag = 1
if a == 0:
    y = e / b
    x = (f - d * y) / c
    flag = 0
if c == 0 and flag:
    y = f / d
    x = (e - b * y) / a
    flag = 0
if b == 0 and flag:
    x = e / a
    y = (f - c * x) / d
    flag = 0

if d == 0 and flag:
    x = f / c
    y = (e - a * x) / b
    flag = 0

if flag:
    y = (f - c * e / a) / (d - b * c / a)
    x = (e - b * y) / a

print(x, y)
