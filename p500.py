from math import log2

def write_primes(output='p500_primes.txt'):
    with open('primes.txt', 'r') as f:
        primes = list(map(int, f.read().split('\n')[:500500]))

    with open(output, 'w') as f:
        for prime in primes:
            f.write(str(prime) + '\n')

    return

def read_primes(input='p500_primes.txt'):
    with open(input, 'r') as f:
        primes = list(map(int, f.read().split('\n')[:-1]))

    return primes

def find_improvement(primes, powers):
    for index1 in reversed(range(1, len(primes))):
        if powers[index1] > 0:
            for index2 in range(index1):
                power_to_add = 2 ** (int(log2(powers[index2] + 1)) + 1) - 1 - powers[index2]
                if primes[index2] ** power_to_add < primes[index1]: return power_to_add, index2, index1

            if powers[index1] == 1: return False

    return False

def main():
    limit = 500500
    primes = read_primes()
    powers = [1 for i in range(limit)]

    counter = 1

    improvement = find_improvement(primes, powers)
    while improvement:
        print(improvement)

        power_to_add, index2, index1 = improvement
        powers[index2] += power_to_add
        powers[index1] -= 1

        counter += 1
        improvement = find_improvement(primes, powers)

    print('Finished finding.')

    result = 1
    for i in range(limit):
        if powers[i] == 0:
            break
        else:
            result *= pow(primes[i], powers[i], 500500507)
            result %= 500500507
            print(result, i)

    print('Final number:', result)

    print('\nFinished.')
    return

if __name__ == '__main__':
    main()
