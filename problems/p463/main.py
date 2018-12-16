def f(n):
    if n == 1: return 1
    if n == 3: return 3
    if n % 2 == 0: return f(n // 2)
    if n % 4 == 1: return 2 * f(2 * (n - 1) // 4 + 1) - f((n - 1) // 4)
    return 3 * f(2 * (n - 3) // 4 + 1) - 2 * f((n - 3) // 4)

limit = 100
for i in range(1, limit + 1): print(i, f(i))
