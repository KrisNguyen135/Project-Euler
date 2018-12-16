from math import sqrt
from fractions import Fraction

def generate_prime_under(limit):
    sieve = [True] * limit
    new_limit = int(sqrt(limit)) + 1

    for i in range(2, new_limit):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False

    return [i for i in range(2, limit) if sieve[i]]

def generate_path(start_pos, length):
    current_list = [[start_pos]]

    for i in range(length - 1):
        temp_list = []

        for path in current_list:
            last_pos = path[-1]

            if last_pos > 1:
                temp_list.append(path + [last_pos - 1])
            if last_pos < 500:
                temp_list.append(path + [last_pos + 1])

        current_list = temp_list

    return current_list

def main():
    target = 'PPPPNNPPPNPPNPN'

    print('Generating primes...')
    primes = generate_prime_under(500)

    pos_to_path_list = {}
    length = len(target)
    for pos in range(1, 501):
        print('Generating paths at', pos)
        pos_to_path_list[pos] = generate_path(pos, length)

    running_prob = Fraction(0, 1)
    for pos in range(1, 501):
        print('Processing path at', pos)
        for path in pos_to_path_list[pos]:
            individual_prob = Fraction(1, 1)
            actual_str = ''

            for num in path:
                if num in primes:
                    actual_str += 'P'
                else:
                    actual_str += 'N'

            for index in range(length):
                if target[index] == actual_str[index]:
                    individual_prob *= Fraction(2, 3)
                else:
                    individual_prob *= Fraction(1, 3)

        running_prob += individual_prob * Fraction(1, len(pos_to_path_list[pos]))

    running_prob *= Fraction(1, 500)

    print(running_prob)

main()
