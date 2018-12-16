from math import sqrt

def generate_primes(limit=1000000000, output='p293_primes.txt'):
    sieve = [True] * limit
    sub_limit = int(sqrt(limit)) + 1

    for i in range(2, sub_limit):
        if sieve[i]:
            print('Sieve looping:', i)
            for j in range(2 * i, limit, i):
                sieve[j] = False

    f = open(output, 'w')
    for i in range(2, limit):
        if sieve[i]:
            print('Writing:', i)
            f.write(str(i) + '\n')
    f.close()

def generate_admissibles(limit=1000000000, output='p293_admissibles.txt'):
    def recur_generate_admissibles(temp_index, temp_admissible):
        print('Current index:', temp_index)
        result = [temp_admissible]
        if temp_admissible * primes[temp_index] < limit:
            result += recur_generate_admissibles(temp_index, temp_admissible * primes[temp_index])
        if temp_admissible * primes[temp_index + 1] < limit:
            result += recur_generate_admissibles(temp_index + 1, temp_admissible * primes[temp_index + 1])

        return result

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27]
    sorted_admissibles = sorted(list(set(recur_generate_admissibles(0, 2))))
    f = open(output, 'w')
    for item in sorted_admissibles:
        f.write(str(item) + '\n')
    f.close()

def solve(input1='p293_primes.txt', input2='p293_admissibles.txt'):
    def get_pseudo_fortunate(admissble, temp_prime_index):
        while primes[temp_prime_index] - admissble < 2:
            temp_prime_index += 1

        return primes[temp_prime_index] - admissble, temp_prime_index

    print('Reading in inputs...')
    primes = list(map(int, open(input1, 'r').read().split('\n')[: -1]))
    admissibles = list(map(int, open(input2, 'r').read().split('\n')[: -1]))

    running_pseudo_fortunate_set = set()
    temp_prime_index = 0
    for admissble in admissibles:
        print('Looping:', admissble)
        temp_pseudo_fortunate, temp_prime_index = get_pseudo_fortunate(admissble, temp_prime_index)
        print(admissble, temp_pseudo_fortunate)
        running_pseudo_fortunate_set.add(temp_pseudo_fortunate)

    print('Set:', running_pseudo_fortunate_set)
    print('Sum:', sum(running_pseudo_fortunate_set))

if __name__ == '__main__':
    #generate_primes(limit=100)
    #generate_primes()

    #generate_admissibles(limit=100)
    #generate_admissibles()

    solve()

    print('Finished.')
