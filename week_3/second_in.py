string = input()
f = 'f'
pos_1 = string.find(f)
flag = 1
k = string.find(f, pos_1)
if pos_1 == -1:
    print(-2)
    flag = 0
if flag:
    pos_2 = string.find(f, pos_1 + 1)
    if pos_2 == -1:
        print(-1)
    else:
        print(pos_2)
