from math import gcd

def solve():
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    def P(s, divisibility_list, limit):
        if divisibility_list[s] == divisibility_list[s + 1]:
            return 0

        return limit // divisibility_list[s] - limit // divisibility_list[s + 1]

    #prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    divisibility_list = [0, 1]
    for i in range(2, 33):
        running_lcm = i
        for j in range(2, i + 1):
            running_lcm = lcm(running_lcm, j)
        divisibility_list.append(running_lcm)

    #for i in range(len(divisibility_list)):
    #    print(i, divisibility_list[i])

    #print(P(3, divisibility_list, 14))
    #print(P(6, divisibility_list, 1000000))

    running_count = 1
    for i in range(2, 32):
        temp_count = P(i, divisibility_list, 4 ** i - 1)
        #print(i, temp_count)
        running_count += temp_count

    print(running_count)

def main():
    solve()

    print('Finished.')
    return

if __name__ == '__main__':
    main()
