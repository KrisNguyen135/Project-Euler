from math import gcd
from timeit import default_timer as timer

def solve1(limit):
    count = 0
    for a in range(1, limit // 3 + 1):
        #print(a)
        for b in range(a, limit // 2 + 1):
            if a + 2 * b > limit: break
            else:
                for c in range(b, min(limit - a - b + 1, a + b)):
                    if a * c % (a + b) == 0: count += 1
    return count

def solve2(limit):
    count = 0
    for a in range(1, limit // 3 + 1):
        #print(a)
        for b in range(a, limit // 2 + 1):
            if a + 2 * b > limit: break
            else:
                divisor = gcd(a, b)
                a_new, b_new = a // divisor, b // divisor
                factor = a_new + b_new
                c_min = - (- b // factor) * factor # hacky way to do ceiling division
                c_max = min(limit - a - b, a + b - 1) // factor * factor
                if c_max >= c_min: count += (c_max - c_min) // factor + 1
    return count

def main():
    limit = 1000
    start = timer()
    count1 = solve1(limit)
    print('Took', timer() - start)
    start = timer()
    count2 = solve2(limit)
    print('Took', timer() - start)
    print(count1, count2, count1 == count2)

main()
