number = int(input())
korov = 'korov'
num_des = number % 10
if number // 10 != 1:
    if num_des == 2 or num_des == 3 or num_des == 4:
        print(number, korov + 'y')
    elif num_des == 1:
        print(number, korov + 'a')
    else:
        print(number, korov)
else:
    print(number, korov)
