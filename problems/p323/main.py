def compute(n):
    temp = 2**n
    return ( (temp-1) / temp ) ** 32 - ( (temp-2) / temp ) ** 32

def solve(num):
    return sum( i * compute(i) for i in range(num) )

print(solve(100))
