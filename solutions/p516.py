from math import sqrt

def get_hammings(limit):
    def recur_get_hammings(temp_num, temp_base_index):
        temp_result = [temp_num]

        for base_index in range(temp_base_index, 3):
            next_num = temp_num * bases[base_index]
            if next_num <= limit:
                temp_result += recur_get_hammings(next_num, base_index)

        return temp_result

    bases = [2, 3, 5]

    hammings = recur_get_hammings(1, 0)
    hammings.sort()

    return hammings

def is_prime(num):
    if num == 2: return True
    elif num % 2 == 0: return False

    limit = int(sqrt(num)) + 1
    for divisor in range(3, limit, 2):
        if num % divisor == 0: return False

    return True

def get_oneplus_primes(hammings, limit):
    result = []
    for hamming in hammings:
        if is_prime(hamming + 1): result.append(hamming + 1)

    return result[3:]

def get_oneplus_hammings(oneplus_primes, limit):
    def recur_get_oneplus_hammings(temp_num, temp_index):
        sub_limit = sqrt(limit)

        temp_result = [temp_num]
        for index in range(temp_index + 1, len(oneplus_primes)):
            if oneplus_primes[index] > sub_limit: break
            else:
                next_num = temp_num * oneplus_primes[index]
                if next_num <= limit: temp_result += recur_get_oneplus_hammings(next_num, index)
                else: break

        return temp_result

    oneplus_hammings = recur_get_oneplus_hammings(1, -1)[1:]
    oneplus_hammings.sort()

    return oneplus_hammings

def get_mixed_hammings(hammings, oneplus_hammings, limit):
    result = []

    sub_limit = limit / oneplus_hammings[0]
    for index1 in range(1, len(hammings)):
        if hammings[index1] > sub_limit: break
        else:
            for index2 in range(len(oneplus_hammings)):
                temp_num = hammings[index1] * oneplus_hammings[index2]
                if temp_num > limit: break
                else:
                    result.append(temp_num)

    result.sort()
    return result

def modular_add(temp_sum, temp_list, mod):
    for item in temp_list:
        temp_sum += item
        temp_sum %= mod

    return temp_sum

if __name__ == '__main__':
    #limit = 1000000000000
    limit = 100
    running_sum = 0
    mod = 4294967296 # 2 ^ 32

    print('Getting normal Hammings...')
    hammings = get_hammings(limit)#; print('Normal Hammings:', hammings)
    print('Adding normal Hammings...')
    running_sum = modular_add(running_sum, hammings, mod)

    print('Getting one-plus primes...')
    oneplus_primes = get_oneplus_primes(hammings, limit)
    print('Getting one-plus hammings...')
    oneplus_hammings = get_oneplus_hammings(oneplus_primes, limit)#; print('One-plus Hammings:', oneplus_hammings)
    print('Adding one-plus Hammings...')
    running_sum = modular_add(running_sum, oneplus_hammings, mod)

    print('Getting mixed Hammings...')
    mixed_hammings = get_mixed_hammings(hammings, oneplus_hammings, limit)#; print('Mixed Hammings:', mixed_hammings)
    print('Adding mixed Hammings...')
    running_sum = modular_add(running_sum, mixed_hammings, mod)

    print(running_sum)

    print('Done.')
