if __name__ == '__main__':
    MOD = 1000000000
    a = 21 ** 7
    b = 7 ** 21
    c = 12 ** 7
    int_b_over_a = b // a

    term1 = (b + 1) % MOD
    term1 = (4 * term1) % MOD
    term1 *= (a - c) % MOD

    term2 = ((b + 1) // 2) % MOD
    term2 *= b % MOD
    term2 %= MOD

    term3 = a % MOD
    term3 *= (4 * a - 3 * c) % MOD
    term3 *= (int_b_over_a // 2) % MOD
    term3 *= (int_b_over_a - 1) % MOD

    term4 = int_b_over_a % MOD
    term4 *= (4 * a - 3 * c) % MOD
    term4 *= (b - int_b_over_a * a + 1) % MOD

    result = (term1 + term2 + term3 + term4) % MOD
    print(result)

    print('Finished.')
