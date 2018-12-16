from random import randint

def simulate(turn_num):
    blue_num = 0
    red_num = 0
    for i in range(turn_num):
        disc = randint(1, i + 2)
        if disc == 1: blue_num += 1
        else: red_num += 1
    if blue_num > red_num: return 1
    return 0

def solve(turn_num):
    result = [1, 1]
    for i in range(turn_num - 1):
        temp_result = [1]
        for j in range(len(result) - 1):
            temp_result.append(result[j] * (i + 2) + result[j + 1])
        temp_result.append(result[-1] * (i + 2))
        result = temp_result
    print(len(result))
    return sum(result[i] for i in range(len(result) // 2)) / sum(result)

'''
test_num = 100000000
turn_num = 15
approximation = sum(simulate(turn_num) for i in range(test_num)) / test_num
print("Approximated probability:", approximation)
result = int(1 / approximation)
print("Final result:", result)
'''

turn_num = 15
probability = solve(turn_num)
print(probability)
print(int(1 / probability))
