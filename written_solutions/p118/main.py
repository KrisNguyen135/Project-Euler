#from math import sqrt
#from collections import Counter
import pandas as pd

#import multiprocessing

def prime_check(n):
    if n < 2:
        return False

    if n % 2 == 0:
        return False

    limit = int(sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True

def custom_permutations(iterable, r):
    pool = iterable
    n = len(pool)

    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield ''.join(pool[i] for i in indices[: r])

    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i :] = indices[i + 1 :] + indices[i : i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield ''.join(pool[i] for i in indices[: r])
                break
        else:
            return

if __name__ == '__main__':
    # generating primes with unique digits
    '''unique_digits_primes = [2, 3, 5, 7]
    digits = '123456789'

    with open('unique_digits_primes.txt', 'w') as f:
        for i in range(2, 10):
            for string_n in custom_permutations(digits, i):
                n = int(string_n)
                if prime_check(n):
                    unique_digits_primes.append(n)
                    f.write(string_n + '\n')'''

    # reduce primes with unique digits
    # by sorting their digits and keep track of the count
    '''with open('unique_digits_primes.txt', 'r') as f:
        unique_digits_string_primes = f.readlines()

    #print(unique_digits_string_primes[-1])
    #print(len(unique_digits_string_primes))

    sorted_string_primes = [''.join(sorted(string_prime[: -1]))
        for string_prime in unique_digits_string_primes]

    #print(sorted_string_primes[-1])
    #print(len(sorted_string_primes))

    counter = Counter(sorted_string_primes)
    #print(counter.most_common(10))

    with open('sorted_string_prime_count.txt', 'w') as f:
        for element, count in counter.most_common():
            f.write(f'{element},{count}\n')'''

    # sorting the sorted-digit primes and adding the length
    '''sorted_string_count_df = pd.read_csv('sorted_string_prime_count.txt',
        header=None, names=['sorted string', 'count'])
    sorted_string_count_df = sorted_string_count_df.sort_values('sorted string',
        ascending=False)

    sorted_string_count_df['length'] = sorted_string_count_df['sorted string'].apply(
        lambda x: len(str(x)))

    #print(sorted_string_count_df.tail(10))
    sorted_string_count_df.to_csv('sorted_string_prime_count_length.txt',
        index=False)'''

    df = pd.read_csv('sorted_string_prime_count_length.txt',
        index_col='sorted string')

    sorted_primes = list(df.index)
    #print(sorted_primes)
    #print(len(sorted_primes))

    running_solutions = [([], '')] # list of (list of sorted primes, concatenated string)
    complete_solutions = [] # list of (list of sorted primes that are complete)

    for sorted_prime in sorted_primes:
        for solution in running_solutions:
            concat_string = solution[1] + str(sorted_prime)

            if len(concat_string) == len(set(concat_string)):
                new_solution = (solution[0] + [sorted_prime],
                    concat_string)

                if len(concat_string) == 9:
                    complete_solutions.append(new_solution[0])
                else:
                    running_solutions.append(new_solution)

        '''print(running_solutions)
        print()
        print(complete_solutions)
        print('*' * 50)'''

    #print(complete_solutions)

    running_result = 0
    for solution in complete_solutions:
        temp_product = 1
        for sorted_prime in solution:
            temp_product *= df.loc[sorted_prime]['count']

        running_result += temp_product

        print(running_result)

    print('Final result:', running_result)
    print('\nFinished.')
