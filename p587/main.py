from math import sqrt, asin, pi

def getArea(n):
    y = (n + 1 - sqrt(2 * n)) / (n ** 2 + 1)
    x = n * y

    area1 = x * y / 2
    area2 = 1 - x + (asin(x - 1) + (x - 1) * sqrt( x * (2 - x))) / 2

    return area1 + area2

def getRatio(n):
    areaL = 1 - pi / 4
    return getArea(n) / areaL

target = 0.001
n = 1
while 1:
    temp = getRatio(n)
    if temp < target: break
    n += 1
print(n)
