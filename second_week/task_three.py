fi, se, th = int(input()), int(input()), int(input())
m = 0
if fi > se:
    se = fi
if se > th:
    th = se
print(th)
