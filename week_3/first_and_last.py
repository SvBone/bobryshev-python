word = input()
f = 'f'
pos = word.find(f)
first = pos
while pos != -1:
    temp = pos
    pos = word.find(f, pos + 1)
try:
    if temp != first:
        print(first, temp)
    else:
        print(first)
except NameError:
    pass
