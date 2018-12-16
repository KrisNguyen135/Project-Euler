from math import sqrt

def getPrimes(limit):
    result = [2, 3]
    if limit < 5: return result
    for i in range(5, limit, 2):
        newLimit = sqrt(i)
        for prime in result:
            if prime > newLimit:
                result.append(i)
                break
            if i % prime == 0: break
    return result

def solve(prime1, prime2, limit):
    result = 0
    exp1 = 1
    temp1 = (prime1 ** exp1) * prime2
    while temp1 <= limit:
        if result < temp1: result = temp1
        exp2 = 2
        temp2 = (prime1 ** exp1) * (prime2 ** exp2)
        while temp2 <= limit:
            if result < temp2: result = temp2
            exp2 += 1
            temp2 = (prime1 ** exp1) * (prime2 ** exp2)
        exp1 += 1
        temp1 = (prime1 ** exp1) * prime2
    return result

limit = 10000000
primes1 = getPrimes(int(sqrt(limit)+1))
primes2 = getPrimes(limit//2)
print("Finished getting primes.")
result = 0
for i in range(len(primes1)):
    print(i, len(primes1))
    for j in range(i+1, len(primes2)):
        result += solve(primes1[i], primes2[j], limit)
print(result)
