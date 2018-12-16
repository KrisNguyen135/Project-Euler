from math import sqrt

def atkin(limit):
    sieve = [True] * limit
    newLimit = int(sqrt(limit)) + 1
    for i in range(2, newLimit):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False
    return [i for i in range(2, limit) if sieve[i]]

def solve(limit):
    primes = atkin(limit)
    result = 0
    for prime in primes:
        square = prime ** 2
        result += (square + 9) // 6 - (square + 13) // 8
    return result * 2

limit = 10 ** 6
print(solve(limit))
