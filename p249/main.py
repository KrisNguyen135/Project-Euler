from math import sqrt

def get_primes(limit):
    sieve = [True] * limit
    new_limit = int(sqrt(limit)) + 1
    for i in range(2, new_limit):
        if sieve[i]:
            for j in range(i * 2, limit, i): sieve[j] = False
    return [i for i in range(2, limit) if sieve[i]]

primes = get_primes(5000)
print(primes)
print(len(primes))
