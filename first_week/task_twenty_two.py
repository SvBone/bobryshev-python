a = int(input())
thous = a // 1000
hundred = (a - thous * 1000) // 100
ten = (a - thous * 1000 - hundred * 100) // 10
one = a % 10
print(thous - one + hundred - ten + 1)
