from math import factorial as fac
from functools import reduce
from operator import mul

def permutation(k, n):
    if k == 0: return 1
    try:
        return reduce(mul, [i for i in range(n - k + 1, n + 1)])
    except TypeError:
        print(k ,n)
        return 0

def p1(k, n):
    return permutation(k, n)

def p2(k ,n):
    result = 0
    maxPairNum = min(k // 2, n)
    for pairNum in range(1, maxPairNum + 1):
        if pairNum % 100 == 0: print(pairNum)
        chooseSlots = permutation(pairNum, n)
        choosePairs = permutation(pairNum * 2, k) // (2 ** pairNum)
        result += choosePairs * chooseSlots * p1(k - pairNum * 2, n - pairNum)
        #print(chooseSlots, choosePairs, result)
    return result

def p(k, n):
    return 1 - (p1(k, n) + p2(k, n)) / (n ** k)

print(p(20000, 1000000))
