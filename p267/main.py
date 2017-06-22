from math import factorial as fac

limit = 432
temp = sum(fac(1000) // fac(i) // fac(1000 - i) for i in range(0, limit))
temp /= 2 ** 1000
print(1 - temp)
