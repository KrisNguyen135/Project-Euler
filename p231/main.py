from math import sqrt
from timeit import default_timer

def get_primes(limit):
    sieve = [True] * limit
    new_limit = int(sqrt(limit)) + 1
    for i in range(2, new_limit):
        if sieve[i]:
            for j in range(i * 2, limit, i): sieve[j] = False
    return [i for i in range(2, limit) if sieve[i]]

def factor(num, primes):
    result = {}
    for prime in primes:
        divisor = prime
        temp_sum = 0
        while divisor <= num:
            temp_sum += num // divisor
            divisor *= prime
        result[prime] = temp_sum
    return result

def solve(upper, lower):
    difference = upper - lower
    primes = get_primes(upper)
    factor_upper = factor(upper, primes)
    factor_lower = factor(lower, primes)
    factor_diff = factor(difference, primes)
    result = {}
    temp_sum = 0
    for prime in primes:
        result[prime] = factor_upper[prime] - factor_lower[prime] - factor_diff[prime]
        temp_sum += prime * result[prime]
    return temp_sum

upper = 2 * (10 ** 7)
lower = 15 * (10 ** 6)
start = default_timer()
print(solve(upper, lower))
print('Took:', default_timer() - start)
