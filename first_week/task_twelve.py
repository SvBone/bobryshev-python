rubles, cops, number = int(input()), int(input()), int(input())
cops = (cops + rubles * 100) * number
rubles = cops // 100
cops -= rubles * 100
print(rubles, cops)
