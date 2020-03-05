a = float(input())
b = float(input())
c = float(input())
ppr = (a + b + c) / 2
s = ((ppr - a) * (ppr - b) * (ppr - c) * ppr) ** 0.5
print(s)
