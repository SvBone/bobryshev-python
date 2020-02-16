x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if (x1 > 0) and (x2 > 0) or (x1 < 0) and (x2 < 0):
    if (y1 > 0) and (y2 > 0) or (y1 < 0) and (y2 < 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
