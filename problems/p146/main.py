from math import sqrt

def check(num, primes):
    square = num ** 2
    if square + 1 not in primes: return False
    if square + 3 not in primes: return False
    if square + 7 not in primes: return False
    if square + 9 not in primes: return False
    if square + 13 not in primes: return False
    if square + 27 not in primes: return False
    return True

def get_primes(limit):
    sieve = [True] * limit
    new_limit = int(sqrt(limit)) + 1
    for i in range(2, new_limit):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False
    return [i for i in range(2, limit) if sieve[i]]

limit = 1000000
primes = get_primes(limit)
print('Finish getting primes')
new_limit = int(sqrt(limit - 27)) + 1
result = 0
for n in range(1, new_limit):
    if check(n, primes):
        print('Found another', n)
        result += n
print('Final result', result)
