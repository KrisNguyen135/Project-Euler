def solve(n):
    if n == 1: return 1777
    result =  1777**(solve(n-1)%1250000)
    print(n)
    return result

print(solve(10))
