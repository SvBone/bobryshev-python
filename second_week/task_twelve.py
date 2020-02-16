x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
logic_1 = (x1 + y1) % 2 == (x2 + y2) % 2
logic_2 = y2 > y1
logic_3 = y2 - y1 >= x2 - x1
if logic_1 and logic_2 and logic_3:
    print('YES')
else:
    print('NO')
