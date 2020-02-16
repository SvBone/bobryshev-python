x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if (x1 + y1) % 2 == (y1 + y2) % 2:
    print("YES")
else:
    print("NO")
