proc = int(input())
rub_x = int(input())
cop_y = int(input())

cops = rub_x * 100 + cop_y

answer = int(cops + cops * proc / 100)
print(answer // 100, answer % 100)
