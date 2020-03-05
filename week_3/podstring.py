string = input()
h = "h"
pos_1 = string.find(h)
flag = pos_1
while flag != -1:
    pos_2 = flag
    flag = string.find(h, flag + 1)

result = string[:pos_1] + string[pos_2 + 1:]
print(result)
