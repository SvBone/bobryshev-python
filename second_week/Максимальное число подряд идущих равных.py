count = 0
max = 1
buf = 0
while True:
    num = int(input())
    if num == 0:
        break
    if buf == num:
        count += 1
    if count > max:
        max = count
    if buf != num:
        count = 1
        buf = num
print(max)
