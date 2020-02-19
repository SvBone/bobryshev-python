number = int(input())
k = 2
while True:
    if number % k != 0:
        k += 1
    else:
        print(k)
        break
