import numpy as np
#import matplotlib.pyplot as plt
from math import log2

def riffle_shuffle(deck, n):
    print('Riffle-shuffling on:')
    print(deck)

    left = deck[: n // 2]
    right = deck[n // 2 :]
    inter = np.ravel(np.column_stack((left, right)))

    print('Left-half:')
    print(left)
    print('Right-half:')
    print(right)
    print('Resulting interleaved deck:')
    print(inter)

    print('Distance between 1 and 2:')
    print(np.where(inter == 2)[0])

    print('Second element, exponentized:')
    print(visualize_two_exponents(inter[1]))

    print('-' * 50)

    return inter

def s(n):
    def get_next_second_element(temp, n):
        if temp % 2 == 0:
            return (temp + n) // 2

        return (1 + temp) // 2

    count = 0
    second_element = 2
    while True:
        second_element = get_next_second_element(second_element, n)
        count += 1
        if second_element == 2:
            break

    return count

def s_v2(n):
    def get_next_two_index(temp, n):
        double = 2 * temp

        if double < n:
            return double

        return double - n + 1

    count = 0
    two_index = 1
    while True:
        two_index = get_next_two_index(two_index, n)
        print(two_index, end=' ')
        count += 1
        if two_index == 1:
            break

    print()
    print('-' * 50)

    return count

def visualize_two_exponents(x):
    result_string = ''
    while x >= 1:
        exponent = int(log2(x))
        result_string += f'2^{exponent} + '
        x -= 2 ** exponent

    return result_string[: -3]

# finding smallest x such that (2 ^ x - 1) is divisible by n
def find_smallest_exponent(n):
    print(f'Finding smallest exponent for {n}')
    i = 1
    power_2 = 2
    while (power_2 - 1) % n != 0:
        i += 1
        power_2 *= 2
        power_2 %= n

    return i

def generate_divisors(coprime_divisors):
    running_divisors = [1]

    for coprime_divisor, power in coprime_divisors:
        new_divisors = []
        for p in range(1, power + 1):
            for divisor in running_divisors:
                new_divisors.append(divisor * (coprime_divisor ** p))

        running_divisors += new_divisors

    return running_divisors

if __name__ == '__main__':
    #n = 62 # n is an even integer

    '''deck = np.arange(1, n + 1)
    for i in range(60):
        deck = riffle_shuffle(deck, n)'''

    #print(s(n))
    #print(s_v2(n))

    '''xs = []
    ys = []
    for i in range(2, 10001, 2):
        xs.append(i)
        ys.append(s(i))
        #print(f'{xs[-1]}: {ys[-1]}')

    #plt.plot(xs, ys)
    #plt.show()

    xs = np.array(xs)
    ys = np.array(ys)

    print(xs[ys == 8])'''

    #print(find_smallest_exponent(7))

    '''coprime_divisors = [(3, 1), (5, 2)] # 75
    divisors = generate_divisors(coprime_divisors)
    print(divisors)
    print(len(divisors))'''

    #TARGET = 8
    TARGET = 60
    N = 2 ** TARGET - 1
    #coprime_divisors = [(3, 1), (5, 1), (17, 1)] # list of (divisor, power)
    coprime_divisors = [(3, 2), (5, 2), (7, 1), (11, 1), (13, 1), (31, 1),
        (41, 1), (61, 1), (151, 1), (331, 1), (1321, 1)]
    divisors = generate_divisors(coprime_divisors)[1 :]

    running_result = 0
    for divisor in divisors:
        temp_exponent = find_smallest_exponent(divisor)
        print(divisor, temp_exponent)

        if temp_exponent == TARGET:
            running_result += divisor + 1

    print('Final result:', running_result)
    print('Finished.')
