ye = int(input())
if ye % 4 == 0 and ye % 100 != 0 or ye % 400 == 0:
    print("YES")
else:
    print("NO")
