num = int(input())
k = []
while num != 0:
    k.append(num)
    num = int(input())
k.sort()
print(k[-2])
