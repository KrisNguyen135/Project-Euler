from math import sqrt
import pandas as pd
import numpy as np

def generate_odd_primes_under(limit):
    sieve = [True for i in range(limit)]

    sub_limit = int(sqrt(limit)) + 1
    for i in range(3, sub_limit, 2):
        print("Prime:", i)
        if sieve[i]:
            for j in range(i * 3, limit, i * 2):
                sieve[j] = False

    odd_primes = [i for i in range(3, limit, 2) if sieve[i]]

    print("Writing to file...")
    pd.Series(odd_primes).to_csv("odd_primes.csv", index=False)

def generate_factorization(limit):
    print("Reading from file...")
    odd_primes = pd.read_csv("odd_primes.csv", header=None)[0].values

    print("Making Pandas...")
    odd_factorization = pd.DataFrame({"num": [i for i in range(3, limit, 2)]})
    odd_factorization = odd_factorization.set_index("num")

    for num in range(3, limit, 2):
        print("Factorization:", num)
        if num in odd_primes:
            odd_factorization.loc[num, 0] = num
        else:
            temp_remains = num
            temp_index = 0

            for prime in odd_primes:
                if temp_remains == 1:
                    print("Break at 1")
                    break
                elif temp_remains % prime == 0:
                    odd_factorization.loc[num, temp_index] = prime
                    temp_index += 1
                    while temp_remains % prime == 0:
                        temp_remains //= prime

    print("Writing to files...")
    odd_factorization.to_csv("odd_factorization.csv")

def solve():
    print("Reading from file...")
    odd_factorization = pd.read_csv("odd_factorization.csv", index_col="num")

    result = 1
    for num in odd_factorization.index:
        print("Solve:", num)
        temp_factors = odd_factorization.loc[num].dropna().astype(int).values
        totient_materials = 1 - 1 / temp_factors
        temp_totient = int(np.prod(totient_materials) * num)

        result += temp_totient

    print("Result:", result)

def main():
    limit = 5 * (10 ** 8)

    #generate_odd_primes_under(limit)

    generate_factorization(limit)

    #solve()

main()
