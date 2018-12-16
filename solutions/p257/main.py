from math import sqrt

def solve(limit):
    next_b = False
    result = limit // 3
    for b in range(1, limit // 2):
        if b % 100 == 0: print(b)
        for c in range(b, min(limit // 2, 2 * b)):
            if next_b:
                next_b = False
                break
            else:
                helper = b ** 2 + c ** 2 + 6 * b * c
                for num in [helper, helper + 4 * b * c]:
                    root = sqrt(num)
                    if root == int(root):
                        a = (int(root) - b - c) // 2
                        if a + b + c > limit: next_b = True
                        elif a + b > c: result += 1
    return result

limit = 10 ** 8
result = solve(limit)
print(result)
