from math import sqrt
from timeit import default_timer as timer

def get_fib(limit):
    sequence = [1, 1]

    phi1 = (1 + sqrt(5)) / 2
    phi2 = (1 - sqrt(5)) / 2

    n = 3
    while sequence[-1] < limit:
        sequence.append(int((phi1 ** n - phi2 ** n) / sqrt(5)))
        n += 1

    return sequence[:-1]

def solve(limit):
    result = [0] * limit
    result[1] = 1

    sequence = get_fib(limit)

    to_use, not_to_use = [[1]], [[1]]

    for element in sequence[2:]:
        #print(element)
        result[element] = 1

        add_list = [[element]]
        drop_index = []
        for i in range(len(to_use)):
            current_term = sum(to_use[i]) + element

            if current_term >= limit: drop_index.append(i)
            else:
                result[current_term] = len(to_use[i]) + 1
                add_list.append(to_use[i] + [element])

        for i in reversed(drop_index): to_use.pop(i)
        to_use += not_to_use
        not_to_use = add_list

    return result

def get_sum(limit):
    sequence = get_fib(limit)
    current_sum = 2
    to_use, not_to_use = [[1]], [[2]]

    for element in sequence[3:]:
        print(element)
        current_sum += 1

        add_list = [[element]]
        drop_index = []
        for i in range(len(to_use)):
            current_term = sum(to_use[i]) + element

            if current_term >= limit: drop_index.append(i)
            elif current_term not in sequence:
                current_sum += len(to_use[i]) + 1
                add_list.append(to_use[i] + [element])

        for i in reversed(drop_index): to_use.pop(i)
        to_use += not_to_use
        not_to_use = add_list

    return current_sum

def get_sum_2(limit):
    sequence = get_fib(limit)
    current_sum = 2

def main():
    limit = 10 ** 17

    '''start = timer()
    result = solve(limit)
    print(sum(result))
    print('Took', timer() - start)'''

    start = timer()
    result_sum = get_sum(limit)
    print(result_sum)
    print('Took', timer() - start)

main()
