def totient(limit):
    sieve = [1] * limit
    for i in range(2, limit):
        #if i % 1000 == 0: print(i)
        if sieve[i] == 1:
            for j in range(i, limit, i):
                sieve[j] *= i - 1
                k = j // i
                while k % i == 0:
                    sieve[j] *= i
                    k //= i
    return sieve

# n > 2
def H(n):
    sieve = totient(n + 1)
    return 6 * (n - 1 + sum(i - 1 - sieve[i] for i in range(3, n + 1)))

limit = 10 ** 8
print(H(limit))
