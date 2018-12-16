from math import sqrt

def generate_primes(limit, output='p407_primes.txt'):
    sub_limit = int(sqrt(limit)) + 1
    sieve = [True for i in range(limit)]

    for i in range(2, sub_limit):
        if sieve[i]:
            for j in range(2 * i, limit, i):
                sieve[j] = False

    with open(output, 'w') as f:
        for i in range(limit):
            if sieve[i]:
                f.write(str(i) + '\n')

    return

def read_primes(input='p407_primes.txt'):
    with open(input, 'r') as f:
        primes = list(map(int, f.read().split('\n')[:-1]))

    return primes

def generate_factorizations(limit, output='p407_factorizations.txt'):
    primes = read_primes()

    sieve = [[] for i in range(limit)]

    for prime in primes:
        print('Looping:', prime)
        for i in range(prime, limit, prime):
            sieve[i].append(prime)

    with open(output, 'w') as f:
        f.write('0\n1\n')
        for i in range(2, limit):
            print('Writing:', i)
            temp_row = ''
            for factor in sieve[i]:
                temp_row += str(factor) + ','
            temp_row = temp_row[:-1]
            temp_row += '\n'

            f.write(temp_row)

    return

def read_factorizations(input='p407_factorizations.txt'):
    factorizations = []

    with open(input, 'r') as f:
        lines = f.read().split('\n')[:-1]
        for line in lines:
            factorizations.append(list(map(int, line.split(','))))

    return

def get_temp_step(num, factor):
    temp_power = 1
    while num % (factor ** temp_power) == 0:
        temp_power += 1

    return factor ** (temp_power - 1)

def generate_steps(input='p407_factorizations.txt', output='p407_steps.txt'):
    input_file = open(input, 'r')
    lines = input_file.read().split('\n')[:-1]
    input_file.close()

    output_file = open(output, 'w')
    output_file.write('0\n1\n')
    for i in range(2, len(lines)):
        print(i)
        temp_factorization = list(map(int, lines[i].split(',')))
        temp_step = max([get_temp_step(i, factor) for factor in temp_factorization])
        output_file.write(str(temp_step) + '\n')

    output_file.close()
    return

def M(num, step):
    for i in range(num - step, 0, - step):
        #print(i)
        if (i * i + i) % num == 0: return i + 1
        if (i * i - i) % num == 0: return i

    return 1

def solve(limit):
    input()
    input()

    result = 0
    for i in range(2, limit):
        temp_step = int(input())
        temp_M = M(i, temp_step)
        print(i, temp_M)

        result += temp_M

    print(result)

def main():
    limit = 10 ** 7 + 1
    #generate_primes(limit)
    #generate_factorizations(limit)

    #generate_steps(input='sample_factorizations.txt')
    #generate_steps()

    solve(limit)

    print('Finished.')
    return

if __name__ == '__main__':
    main()
