from math import sqrt

limit = 12
i = 2
while limit > 0:
    if i % 1000000 == 0: print(i)
    temp = sqrt(5 * (i**2) - 1)
    if temp == int(temp):
        a = (temp - 2) / 5
        b = (temp + 2) / 5
        if a == int(a):
            limit -= 1
            print(limit)
        if b == int(b):
            limit -= 1
            print(limit)
    i += 1

print(i - 1)
