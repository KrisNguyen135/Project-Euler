from math import sqrt

def getPrimes(limit):
    sieve = [True] * limit
    newLimit = int(sqrt(limit)) + 1
    for i in range(2, newLimit):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False
    return [i for i in range(2, limit) if sieve[i]]

limit = 10 ** 8
primes = getPrimes(limit)
result = 0
for i in range(len(primes) - 2):
    print('out:', i, len(primes))
    for j in range(i + 1, len(primes) - 1):
        print('in:', j, len(primes))
        temp = ((primes[j] + 1) ** 2) / (primes[i] + 1) - 1
        if temp > limit: break
        elif temp == int(temp) and int(temp) in primes: result += primes[i] + primes[j] + int(temp)
print(result)
