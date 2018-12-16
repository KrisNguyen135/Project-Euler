# using sieve
from math import sqrt, gcd

def get_sieve(limit):
    sieve = [1] * limit
    # looping through to find every a^2+b^2 and add to sieve
    a_limit = int(sqrt(limit / 2)) + 1
    for a in range(1, a_limit):
        # handling adding when a=b
        sos_dup = 2 * (a ** 2)
        sieve[sos_dup] += 2 * a
        for i in range(sos_dup * 2, limit, sos_dup): sieve[i] += i // sos_dup * 2 * a + 2 * a
        b = a + 1
        sos = a ** 2 + b ** 2
        while sos < limit:
            # handling adding the pair more than once when i // sos is a square
            if gcd(a, b) == 1:
                # for each pair we're adding (a-b)+(a+b)+(b-a)+(b+a) multiplied by i // sos
                # so we're essentially considering i // sos * a and i // soc * b
                for i in range(sos, limit, sos): sieve[i] += i // sos * 2 * (a + b)
            b += 1
            sos = a ** 2 + b ** 2
    # adding divisors of a number to the sieve at that number
    for i in range(2, limit):
        for j in range(i, limit, i): sieve[j] += i
    return sieve

limit = 100001
sieve = get_sieve(limit)
#for i in range(1, limit): print(i, sieve[i])
print(sum(sieve[1:]))
