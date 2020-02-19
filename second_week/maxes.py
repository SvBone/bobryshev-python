num = int(input())
k = []
while num != 0:
    k.append(num)
    num = int(input())
k.sort()
count = 0
for i in k:
    if i == k[-1]:
        count += 1
print(count)
