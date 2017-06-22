# read about nim-sum
# problems becomes finding the number of binaries
# less than 2^30 that don't that adjacent 1's

def solve(n):
    if n == 1: return (1, 1)
    temp = solve(n - 1)
    return (temp[0] + temp[1], temp[0])

print(sum(solve(30)))
