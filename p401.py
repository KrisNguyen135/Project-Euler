from timeit import default_timer as timer

def SIGMA2(limit, mod):
    running_sum = 0

    for divisor in range(1, limit + 1):
        #print(divisor)
        running_sum += pow(divisor, 2, mod) * (limit // divisor)
        running_sum %= mod

    return running_sum

def SIGMA2_v2(limit, mod):
    running_sum = 0

    for divisor in range(1, mod + 1):
        multiplier = limit // divisor
        for term_to_add in range(mod, limit, mod):
            multiplier += limit // (divisor + term_to_add)

        running_sum += pow(divisor, 2, mod) * multiplier
        running_sum %= mod

    return running_sum

def SIGMA2_v3(limit, mod):
    running_sum = 0

    for divisor in range(1, mod // 2):
        multiplier = limit // divisor

        inverse_divisor = mod - divisor
        inverse_multiplier = limit // inverse_divisor

        for term_to_add in range(mod, limit, mod):
            multiplier += limit // (divisor + term_to_add)
            inverse_multiplier += limit // (inverse_divisor + term_to_add)

        running_sum += pow(divisor, 2, mod) * (multiplier + inverse_multiplier)
        running_sum %= mod

    return running_sum

def SIGMA2_v4(limit, mod):
    running_sum = 0

    for divisor in range(1, mod // 2):
        print(divisor)

        multiplier = limit // divisor

        inverse_divisor = mod - divisor
        inverse_multiplier = limit // inverse_divisor

        for term_to_add in range(mod, limit // 2, mod):
            multiplier += limit // (divisor + term_to_add)
            inverse_multiplier += limit // (inverse_divisor + term_to_add)

        term_to_add = limit // mod - (limit // 2) // mod
        multiplier += term_to_add
        inverse_multiplier += term_to_add

        running_sum += pow(divisor, 2, mod) * (multiplier + inverse_multiplier)
        running_sum %= mod

    return running_sum

def main():
    limit = 10 ** 15
    #limit = 6
    mod = 10 ** 9

    '''start = timer()
    print(SIGMA2(limit, mod))
    print('Took', timer() - start, '\n')

    start = timer()
    print(SIGMA2_v2(limit, mod))
    print('Took', timer() - start, '\n')

    start = timer()
    print(SIGMA2_v3(limit, mod))
    print('Took', timer() - start, '\n')'''

    start = timer()
    print(SIGMA2_v4(limit, mod))
    print('Took', timer() - start, '\n')

main()
