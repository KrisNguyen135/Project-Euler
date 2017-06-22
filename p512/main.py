def totientOdd(limit):
    sieve = [1] * limit
    for i in range(3, limit, 2):
        if i % 1000 == 1: print(i)
        if sieve[i] == 1:
            for j in range(i, limit, i):
                sieve[j] *= i - 1
                k = j // i
                while k % i == 0:
                    sieve[j] *= i
                    k //= i
    return sieve

def solve(limit):
    sieve = totientOdd(limit + 1)
    return sum(sieve[i] for i in range(1, limit + 1, 2))

#limit = 100
limit = 5 * (10 ** 8)
print(solve(limit))
