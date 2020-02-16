first, second = int(input()), int(input())
yestr = 'YES'*(1-(first % second))
nostr = 'NO'*((((first % second)+2)//((first % second)+1)) % 2)
print(yestr + nostr)
