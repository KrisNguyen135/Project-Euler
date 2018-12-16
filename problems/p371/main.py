import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def prob(n):
    return 500 * nCr(499, n-1) * (2 ** (n-1)) / nCr(1000, n)

print(sum(prob(i) for i in range(1, 501)))
