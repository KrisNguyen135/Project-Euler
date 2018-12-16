def getPrimes(limit):
    n = [0]*(limit)
    for i in range(2, limit//2):
        for j in range(i*2, L, i):
            n[j] += 1
    return [i for i in range(2, limit) if n[i] == 0]

# num has to be of the form (p-1) and (2q-4) with p, q prime
def test1(num):
    limit = sqrt(num)

L = (10**7)*2
primes = getPrimes(L)
