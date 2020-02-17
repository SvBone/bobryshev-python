a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

# Большее к большему
if a1 > b1:
    a1, b1 = b1, a1
if b1 > c1:
    b1, c1 = c1, b1
if a1 > b1:
    a1, b1 = b1, a1

if a2 > b2:
    a2, b2 = b2, a2
if b2 > c2:
    b2, c2 = c2, b2
if a2 > b2:
    a2, b2 = b2, a2

# первый вариант расположения
num_a = a1 // a2
num_b = b1 // b2
num_c = c1 // c2
res_first = num_a * num_b * num_c

# второй вариант расположения
num_a = a1 // a2
num_b = b1 // c2
num_c = c1 // b2
res_second = num_a * num_b * num_c

# третий вариант расположения
num_a = a1 // b2
num_b = b1 // a2
num_c = c1 // c2
res_third = num_a * num_b * num_c

# четвертый вариант расположения

num_a = a1 // b2
num_b = b1 // c2
num_c = c1 // a2
res_fourth = num_a * num_b * num_c

# пятый вариант расположения

num_a = a1 // c2
num_b = b1 // a2
num_c = c1 // b2
res_fivth = num_a * num_b * num_c

# шестой вариант расположения

num_a = a1 // c2
num_b = b1 // b2
num_c = c1 // a2
res_sixth = num_a * num_b * num_c

maximum = 0

if res_first > maximum:
    maximum = res_first
if res_second > maximum:
    maximum = res_second
if res_third > maximum:
    maximum = res_third
if res_fourth > maximum:
    maximum = res_fourth
if res_fivth > maximum:
    maximum = res_fivth
if res_sixth > maximum:
    maximum = res_sixth
print(maximum)
