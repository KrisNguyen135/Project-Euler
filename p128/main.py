'''def solve(innerLayer, center1, num1, center2, num2):
    a = abs(center2 - num2) - abs(center1 - num1)
    b = abs(center1 - num1) - a * innerLayer
    return (a, b)

innerLayer = int( input("inner layer number: ") )
center1 = int( input("center 1: ") )
num1 = int( input("num 1: ") )
center2 = int( input("center 2: ") )
num2 = int( input("num 2: ") )

result = solve(innerLayer, center1, num1, center2, num2)
print("Final function: (%s)n + (%s)" % result)
'''

from math import sqrt
from itertools import count, islice

def primeTest(n):
    return n > 1 and all( n % i for i in islice(count(2), int(sqrt(n)-1)) )

def specialTest(layerNum):
    common = primeTest(6*layerNum - 7)
    return (primeTest(6*layerNum-5) and primeTest(12*layerNum-7) and common, primeTest(6*layerNum-1) and primeTest(12*layerNum-19) and common)

initials = [1, 2, 8, 19]

def solve(limit):
    limit -= len(initials)
    if limit <= 0: return initials[limit - 1 + len(initials)]
    layerNum = 3
    while limit > 0:
        #print(limit)
        layerNum += 1
        result = specialTest(layerNum)
        if result[0]: limit -= 1
        if result[1]: limit -= 1
    if limit == -1: return 3 * (layerNum**2) - 9*layerNum + 8
    return 3 * (layerNum**2) - 3*layerNum + 1

target = 2000
print(solve(target))
