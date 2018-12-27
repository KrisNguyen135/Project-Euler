from math import sqrt
from decimal import Decimal

SQRT_5 = sqrt(5)
MOD = 1307674368000

def custom_pow(x, exponent, mod=MOD):
    sign = -1 if x < 0 else 1

    abs_x = abs(x)

    result = abs_x - (abs_x // mod) * mod
    power_count = 1

    while result > 1 and power_count < exponent:
        result *= abs_x
        #result -= (result // mod) * mod
        if result > mod:
            result -= (result // mod) * mod

        power_count += 1

    if power_count < exponent:
        result = result ** (exponent - power_count)

    return result * sign

def pow_of_10_to_15(x, mod=MOD):
    #print('Processing', x)

    abs_x = abs(x)
    result = Decimal(abs_x)

    for i in range(15):
        print(f'{i}-th iteration: {result}')

        '''result **= 2
        result -= (result // mod) * mod
        result **= 5
        result -= (result // mod) * mod'''

        multiplier = result
        for j in range(10):
            print(f'\t{j}-th sub-iteration: {result}')
            result *= multiplier
            if result > mod:
                result -= (result // mod) * mod

    return result

def F(x, n, mod=MOD, final_n=False):
    denominator = x ** 2 + x - 1

    sum = x / denominator
    difference = (2 * (x ** 2) + x) / denominator / SQRT_5

    A = (sum + difference) / 2
    B = sum - A

    phi1 = (1 + SQRT_5) / 2 * x
    phi2 = (1 - SQRT_5) / 2 * x

    if final_n:
        #print(pow_of_10_to_15(phi1))
        #print(pow_of_10_to_15(phi2))
        return int(float(pow_of_10_to_15(phi1)) * A\
            + float(pow_of_10_to_15(phi2)) * B - sum) % mod

    return int(custom_pow(phi1, n) * A\
        + custom_pow(phi2, n) * B - sum) % mod

if __name__ == '__main__':
    '''print(f'F_1(1): {F(1, 1)}')
    print(f'F_1(2): {F(2, 1)}')

    print(f'F_2(1): {F(1, 2)}')
    print(f'F_2(2): {F(2, 2)}')

    print(f'F_7(11): {F(11, 7)}')'''


    #print(pow_of_10_to_15((1 + SQRT_5) * 50))

    #print(F(100, 10 ** 15, final_n=True))
    print(pow_of_10_to_15(2, mod=1050))

    '''running_sum = 0
    for i in range(101):
        temp = F(i, 10 ** 15, final_n=True)
        print(f'{i}: {temp}')
        running_sum += temp
        running_sum %= MOD

    print('Final result:', running_sum)'''


    print('Finished.')
