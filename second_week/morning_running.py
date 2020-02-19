first_distantion = int(input())
second_distantion = int(input())
days = 1
while True:
    if first_distantion < second_distantion:
        days += 1
        first_distantion *= 1.1
    else:
        print(days)
        break
