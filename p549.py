from copy import deepcopy
from math import log
import numpy as np

def read_primes(input='primes.txt'):
    with open(input, 'r') as f:
        primes = list(map(int, f.read().split('\n')[:-1]))

    return primes

def generate_factorizations(limit=100000001, input='primes.txt', output='p549_factorizations.txt'):
    factorizations = [[] for i in range(limit)]

    input_file = open(input, 'r')
    for line in input_file:
        temp_prime = int(line[:-1])
        print('Looping:', temp_prime)
        for i in range(temp_prime, limit, temp_prime):
            factorizations[i].append(temp_prime)
    input_file.close()

    output_file = open(output, 'w')
    output_file.write('0\n1\n')
    for i in range(2, limit):
        print('Writing:', i)
        temp_row = ''
        for factor in factorizations[i]:
            temp_row += str(factor) + ','
        temp_row = temp_row[:-1]
        output_file.write(temp_row + '\n')
    output_file.close()

    return

def old_solve(limit=100000001, prime_input='primes.txt', factorization_input='p549_factorizations.txt'):
    def get_factorial_factor(num, factor):
        running_power = 0
        temp_divisor = factor
        while num >= temp_divisor:
            running_power += num // temp_divisor
            temp_divisor *= factor

        return factor ** running_power

    def get_best_divisors(num, factorization, primes):
        main_divisor_list = []
        extra_divisor_list = []

        for prime in primes:
            if prime > num:
                break
            elif prime in factorization:
                main_divisor_list.append(get_factorial_factor(num, prime))
            else:
                extra_divisor_list.append(get_factorial_factor(num, prime))

        return main_divisor_list, extra_divisor_list

    def get_best_divisors_v2(num, factorization, primes):
        divisor_list = []
        for prime in primes:
            if prime > num:
                break
            else:
                divisor_list.append(get_factorial_factor(num, prime))

        return divisor_list

    def get_divisors(num, factorization, primes, limit=limit):
        def recur_get_divisors(temp_divisor, remaining_divisor_list, limit=limit):
            if temp_divisor > limit:
                return []

            temp_divisor_list = [temp_divisor]
            for i in range(len(remaining_divisor_list)):
                new_divisor_list = deepcopy(remaining_divisor_list[i + 1:])
                #temp_divisor_list += recur_get_divisors(temp_divisor, new_divisor_list)
                temp_divisor_list += recur_get_divisors(temp_divisor * remaining_divisor_list[i], new_divisor_list)

            return temp_divisor_list

        #main_divisor_list, extra_divisor_list = get_best_divisors(num, factorization, primes)
        best_divisor_list = get_best_divisors_v2(num, factorization, primes)
        print(num, best_divisor_list)
        #starting_
        return recur_get_divisors(1, best_divisor_list, limit=limit)[1:]

    primes = read_primes(input=prime_input)

    input_file = open(factorization_input, 'r')
    next(input_file); next(input_file)

    i = 2
    for line in input_file:
        temp_factorization = list(map(int, line.split(',')))
        divisor_list = get_divisors(i, temp_factorization, primes, limit=limit)
        print(i, divisor_list)

        i += 1

    #get_best_divisors(6, [2, 3], primes)
    #get_divisors(6, [2, 3], primes)

def new_solve(limit=100000001, prime_input='primes.txt', factorization_input='p549_factorizations.txt'):
    def power_solve(limit=limit, prime_input=prime_input):
        print('Initializing s...')
        s = np.zeros(limit).astype(int); s[0] = -1; s[1] = 1

        print('Reading in primes...')
        primes = read_primes(input=prime_input)

        for prime in primes:
            print('Prime-looping:', prime)
            sub_limit = int(log(limit, prime))
            sub_s = np.zeros(sub_limit).astype(int)

            temp_power = 1
            temp_step = prime
            while temp_power <= sub_limit:
                for i in range(temp_step, sub_limit * prime + 1, temp_step):
                    sub_s[i // prime - 1:] += 1

                temp_power += 1
                temp_step *= prime

            #print(sub_s)

            sub_s_index = 0
            while sub_s[sub_s_index] < sub_limit:
                #print('Sub_s index:', sub_s_index)
                s_index = prime ** sub_s[sub_s_index]
                while s[s_index] == 0:
                    s[s_index] = (sub_s_index + 1) * prime
                    s_index //= prime

                sub_s_index += 1

            s_index = prime ** sub_limit
            while s[s_index] == 0:
                s[s_index] = (sub_s_index + 1) * prime
                s_index //= prime

        return s

    def get_factorization_power(num, factor):
        temp_power = 0
        temp_divisor = factor
        while num % temp_divisor == 0:
            temp_power += 1
            temp_divisor *= factor

        return temp_power

    print('Start power-solving...')
    s = power_solve()
    #print(s)
    print('Finished power-solving. Start reading in factorizations...')

    f = open(factorization_input, 'r'); next(f); next(f)
    temp_num = 2
    for line in f:
        print('Factor-looping:', temp_num)
        temp_factorization = list(map(int, line.split(',')))
        factorization_power = [get_factorization_power(temp_num, factor) for factor in temp_factorization]

        if s[temp_num] == 0:
            s[temp_num] = max(s[temp_factorization[i] ** factorization_power[i]] for i in range(len(temp_factorization)))

        temp_num += 1

    #print(s)
    print('Final answer:', s.sum())

def main():
    #generate_factorizations(limit=101, input='sample_primes.txt')
    #generate_factorizations()

    #old_solve(limit=101, prime_input='sample_primes.txt')
    #new_solve(limit=101, prime_input='sample_primes.txt')
    new_solve()

    print('Finished.')
    return

if __name__ == '__main__':
    main()
