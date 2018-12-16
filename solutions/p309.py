from math import sqrt

def solve(limit):
    w_limit = int(limit // sqrt(2)) + 1
    w_result = {}

    for w1 in range(3, w_limit):
        w2 = w1 + 1
        helper = sqrt(w1 ** 2 + w2 ** 2)
        while helper < limit:
            if helper == int(helper):
                if w1 in w_result: w_result[w1].append(w2)
                else: w_result[w1] = [w2]

                if w2 in w_result: w_result[w2].append(w1)
                else: w_result[w2] = [w1]

            w2 += 1
            helper = sqrt(w1 ** 2 + w2 ** 2)

    #print('\n', w_result, '\n')
    #for key in w_result: print(len(w_result[key]))

    result = 0

    for key in w_result:
        for i1 in range(len(w_result[key]) - 1):
            for i2 in range(i1 + 1, len(w_result[key])):
                if w_result[key][i1] * w_result[key][i2] % (w_result[key][i1] + w_result[key][i2]) == 0: result += 1

    return result

def solve_v2(limit):
    w_limit = int(limit // sqrt(2)) + 1

    result = 0

    for w1 in range(3, w_limit):
        current_list = []

        w2 = w1 + 1
        helper = sqrt(w1 ** 2 + w2 ** 2)
        while helper < limit:


def main():
    limit = 200
    result = solve(limit)
    print(result)

main()
