def fac_trailing_zero_num(n):
    cur_sum = 0
    divisor = 5
    while divisor < n:
        cur_sum += n // divisor
        divisor *= 5
    return cur_sum

def denominator_trailing_zero_num(i, k):
    assert(i >= k)
    return sum(fac_trailing_zero_num(item) for item in [200000 - i, i - k, k])

#print(fac_trailing_zero_num(200000))
result = 0
for i in range(200001):
    if i % 100 == 0: print('i:', i)
    for k in range(i + 1):
        if denominator_trailing_zero_num(i, k) < 49987: result += 1
print(result)
