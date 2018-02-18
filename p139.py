from math import sqrt, gcd

def solve(limit):
    count = 0
    running_set = set()

    c_limit = limit / (1 + sqrt(2))

    c = 0
    m = 2

    while c < limit:
        print(m)
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > c_limit:
                break
            elif c % (b - a) == 0:
                temp_gcd = gcd(a, b)
                temp_triangle = frozenset([a, b, c])
                if temp_gcd == 1 and temp_triangle not in running_set:
                    count += limit // (a + b + c)
                    running_set.add(temp_triangle)

        m += 1

    #print(running_set)
    return count
    #return len(running_set)

if __name__ == '__main__':
    result = solve(10 ** 8)
    print('Final result:', result)

    print('Finished.')
