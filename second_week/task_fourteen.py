first, second, third = int(input()), int(input()), int(input())
logic_1 = (first % 2 == 0 or second % 2 == 0 or third % 2 == 0)
logic_2 = (first % 2 == 1 or second % 2 == 1 or third % 2 == 1)
if logic_1 and logic_2:
    print('YES')
else:
    print('NO')
