from timeit import default_timer as timer
from math import log

def B(n):
    def recur_B(n):
        if n in result: return result[n]

        temp_result = 1
        index1 = (n + 1) // 2 - 1
        index2 = n - (n + 1) // 2
        temp_result += (index1 * recur_B(index1) + index2 * recur_B(index2)) / n

        result[n] = temp_result
        return temp_result

    result = {0: 0, 1: 1}
    return recur_B(n)

def R(n):
    '''temp_result = sum(i / (i + 1) / (i + 2) for i in range(1, n))

    return 1 + 2 * (n + 1) * temp_result / n'''

    running_sum = 0
    for i in range(1, n):
        #print(i)
        running_sum += i / (i + 1) / (i + 2)

    return 1 + 2 * (n + 1) * running_sum / n

def R_v2(n):
    running_sum = 0
    for i in range(3, n + 1):
        #print(i)
        running_sum += 1 / i

    running_sum = 2 / (n + 1) + running_sum - 1 / 2

    return 1 + 2 * (n + 1) * running_sum / n

def R_v3(n):
    running_sum = log(n) - 1.5 + 0.5772156649 + 1 / 2 / n
    return 3 / n + 2 * (n + 1) * running_sum / n


if __name__ == '__main__':
    '''target = 10000000000

    print('Computing R...')
    #r = R(target)
    r = R_v2(target)
    print('Computing B...')
    b = B(target)

    print('Final result:', r - b)
    print('Done.')'''

    '''for i in range(1000, 1010):
        print(R(i), R_v2(i), R_v3(i))'''

    '''target = 1000000

    start = timer()
    result = R(target)
    print(timer() - start)

    start = timer()
    result = R_v2(target)
    print(timer() - start)'''

    target = 10000000000
    r = R_v3(target)
    b = B(target)
    print(r - b)
