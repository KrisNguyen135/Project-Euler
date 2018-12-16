from itertools import combinations
from math import factorial

def solve():
    running_count = 0

    for ordered_com in set(combinations('99887766554433221100', 10)):
        if (90 - 2 * sum(int(digit) for digit in ordered_com)) % 11 == 0:
            pair_num = 10 - len(set(digit for digit in ordered_com))
            zero_count = ordered_com.count('0')

            no_zero_result = factorial(10) // (2 ** pair_num)
            one_zero_result = no_zero_result - factorial(9) // (2 ** pair_num)
            two_zero_result = no_zero_result - factorial(9) // (2 ** (pair_num - 1))

            if zero_count == 0:
                running_count += no_zero_result * no_zero_result
            elif zero_count == 1:
                running_count += no_zero_result * one_zero_result
            else:
                running_count += no_zero_result * two_zero_result

    print(running_count)

def main():
    solve()

main()
