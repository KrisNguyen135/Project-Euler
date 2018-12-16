if __name__ == '__main__':
    n = 100000007
    k = 10007
    MOD = 100000000

    base = pow(2, 10000, MOD)

    two_to_n_k = pow(base, 9999, MOD)
    two_to_n = (base * two_to_n_k * (2 ** 7)) % MOD

    numerator = two_to_n * (k - 1) + n - k + 1
    numerator %= MOD
    numerator *= two_to_n_k
    numerator %= MOD

    denominator = pow(two_to_n - 1, 2, MOD)

    result = (numerator * denominator) % MOD
    print(result)

    print('Finished.')
