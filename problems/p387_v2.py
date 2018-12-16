from math import sqrt

def get_primes_under(limit):
    sieve = [True] * limit
    new_limit = int(sqrt(limit)) + 1

    for i in range(2, new_limit):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False

    return [i for i in range(2, limit) if sieve[i]]

def heavy_prime_test(num, primes):
    limit = sqrt(num)

    for prime in primes:
        if prime > limit:
            break
        elif num % prime == 0:
            return False

    return True

def get_rt_Harshad(digit_limit):
    final_result = {1: list(range(1, 10))}

    for current_digit_num in range(2, digit_limit + 1):
        current_result = []

        for num in final_result[current_digit_num - 1]:
            current_result.append(num * 10)

            current_sum = sum(int(char) for char in str(num))
            for digit in range(1, 10):
                new_num = int(str(num) + str(digit))

                if new_num % (current_sum + digit) == 0:
                    current_result.append(new_num)

        final_result[current_digit_num] = current_result

    return final_result

def get_srt_Harshad_primes(digit_limit):
    testing_digits = [1, 3, 7, 9]

    #running_result = []
    running_sum = 0

    primes = get_primes_under(10 ** (digit_limit // 2))
    #print('Primes:')
    #print(primes)

    rt_Harshad = get_rt_Harshad(digit_limit - 1)
    #print('Right truncatable Harshad:')
    #print(rt_Harshad)

    for current_digit_num in range(2, digit_limit // 2):
        for num in rt_Harshad[current_digit_num]:
            current_quotient = num // sum(int(char) for char in str(num))

            if current_quotient in primes:
                for digit in testing_digits:
                    new_num = int(str(num) + str(digit))

                    if new_num in primes:
                        #print('In prime test:', new_num)
                        #running_result.append(new_num)
                        running_sum += new_num

    for num in rt_Harshad[digit_limit // 2]:
        current_quotient = num // sum(int(char) for char in str(num))

        if current_quotient in primes:
            for digit in testing_digits:
                new_num = int(str(num) + str(digit))

                if heavy_prime_test(new_num, primes):
                    #print('Fusion prime test:', new_num)
                    #running_result.append(new_num)
                    running_sum += new_num

    for current_digit_num in range(digit_limit // 2 + 1, digit_limit):
        for num in rt_Harshad[current_digit_num]:
            current_quotient = num // sum(int(char) for char in str(num))

            if heavy_prime_test(current_quotient, primes):
                for digit in testing_digits:
                    new_num = int(str(num) + str(digit))

                    if heavy_prime_test(new_num, primes):
                        #print('Heavy prime test:', new_num)
                        #running_result.append(new_num)
                        running_sum += new_num

    #return running_result, running_sum
    return running_sum

def main():
    digit_limit = 14
    result = get_srt_Harshad_primes(digit_limit)

    print(result)

main()
