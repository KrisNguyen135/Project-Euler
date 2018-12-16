def get_sequence(limit):
    sieve = [1] * 2000
    if limit < 2000: return sieve[:limit]
    for i in range(2000, limit): sieve.append(sieve[i - 2000] + sieve[i - 1999])
    return sieve

limit = 4005
sequence = get_sequence(limit)
print(sequence[-10:])

'''
k = 10 ** 8
print(pow(2, k // 2000, 20092010))
'''
