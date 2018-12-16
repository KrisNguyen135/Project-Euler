def collatz(num, string):
    if num == 1: return string
    divisor = num % 3
    if divisor == 0: return collatz(num // 3, string + 'D')
    if divisor == 1: return collatz((4 * num + 2) // 3, string + 'U')
    return collatz((2 * num - 1) // 3, string + 'd')

num = 231
result = collatz(num, '')
print(result)
