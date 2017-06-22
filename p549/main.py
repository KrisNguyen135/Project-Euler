def get5(num):
    sum = 0
    divisor = 5
    while divisor <= num:
        sum += num // divisor
        divisor *= 5
    return sum

num = 50
print(get5(num))
