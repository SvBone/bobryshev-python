f = float(input())
ost = int(f * 10) % 10
if ost >= 5:
    print(int(f) + 1)
else:
    print(int(f))
