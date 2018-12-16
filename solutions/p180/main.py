from fractions import *
from math import sqrt

order = 10
mySet = set()

def get():
    for n1 in range(1, order+1):
        print(n1)
        for n2 in range(1, order+1):
            for d1 in range(1, order+1):
                for d2 in range(1, order+1):
                    x = Fraction(n1, d1)
                    y = Fraction(n2, d2)

                    z1 = x + y
                    if z1.denominator < 36 and z1.numerator < 36: mySet.add(x + y + z1)

                    z2 = 1/x + 1/y
                    if z2.denominator < 36 and z2.numerator < 36: mySet.add(x + y + 1/z2)

                    z3 = (x ** 2) + (y ** 2)
                    n3 = sqrt(z3.numerator)
                    d3 = sqrt(z3.denominator)
                    if n3 == int(n3) and d3 == int(n3):
                        z3 = Fraction(int(n3), int(d3))
                        if z3.denominator < 36 and z3.numerator < 36: mySet.add(x + y + z3)

                    z4 = 1 / (x ** 2) + 1 / (y ** 2)
                    n4 = sqrt(z4.numerator)
                    d4 = sqrt(z4.denominator)
                    if n4 == int(n4) and d4 == int(d4):
                        z4 = Fraction(int(n4), int(d4))
                        if z4.denominator < 36 and z4.numerator < 36: mySet.add(x + y + 1/z4)

get()
print('Done processing.')
result = sum(mySet)
print(result)
print(result.denominator + result.numerator)
