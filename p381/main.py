from math import sqrt

def getPrimes(limit):
    sieve = [True] * limit
    newLimit = int(sqrt(limit)) + 1
    for i in range(2, newLimit):
        #print(i, newLimit)
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False
    return [i for i in range(2, limit) if sieve[i]]

def S(p):
    x = 0
    for k in range(1, 24):
        temp = k * p - 1
        if temp % 24 == 0:
            x = temp // 24
            break
    return 9 * x % p

def solve(limit):
    primes = getPrimes(limit)
    result = sum(S(prime) for prime in primes)
    #for prime in primes: result += S(prime)
    return result

limit = 10 ** 8
print(solve(limit))
