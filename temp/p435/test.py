mod = 1050
result = 2

for i in range(15):
    print(f'{i}-th iteration: {result}')

    result = pow(result, 10, mod)

print(result)
