a, b, c = int(input()), int(input()), int(input())
c_kv = c ** 2
a_kv = a ** 2
b_kv = b ** 2
cos_a = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
cos_b = (c ** 2 + a ** 2 - b ** 2) / (2 * a * c)
cos_c = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
logic_pry = c_kv == a_kv + b_kv or a_kv == c_kv + b_kv or b_kv == c_kv + a_kv
logic_nev = (a >= b + c) or (b >= a + c) or (c >= a + b)
logic_ost = (cos_a > 0) and (cos_b > 0) and (cos_c > 0)
logic_tup = not logic_ost
if logic_pry:
    print('rectangular')
elif logic_nev:
    print('impossible')
elif logic_ost:
    print('acute')
elif logic_tup:
    print('obtuse')
