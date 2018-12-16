from numpy import array

def solve(n):
    if n == 3:
        result = []
        for firstNum in range(10):
            result.append([])
            for secondNum in range(10):
                if firstNum + secondNum > 9: result[firstNum].append(0)
                else: result[firstNum].append(10 - firstNum - secondNum)
        return array(result)

    prevResult = solve(n-1)
    result = array( [ [0]*10 ]*10 )

    for firstNum in range(10):
        for secondNum in range(10):
            temp = 10 - firstNum - secondNum
            for i in range(temp): result[i][firstNum] += prevResult[firstNum][secondNum]

    print(n)
    return result

result = solve(20)
final = 0
for i in range(1,10):
    for j in range(10):
        final += result[i][j]

print(final)
