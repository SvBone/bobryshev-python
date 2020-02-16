 a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d and (b <= e or c <= 0):
    print("YES")
elif a <= e and (b <= d or c <= d):
    print("YES")
elif b <= d and (a <= e or c <= e):
    print("YES")
elif b <= e and (a <= d or c <= d):
    print("YES")
else:
    print("NO")
