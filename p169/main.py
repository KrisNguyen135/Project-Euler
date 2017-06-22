import numpy as np

# finds all possible representations
# starting with 0 and 1
# using brute force
def solveBF(currentString, currentList):
    result = np.array([0, 0])

    if currentString[0] == '0': result += np.array([1, 0])
    else: result += np.array([0, 1])

    for i in range(len(currentString)-1):
        if currentString[i] != '0' and currentString[i+1] == '0':
            temp = currentString[:i] + str(int(currentString[i])-1) + '2' + currentString[i+2:]

            if temp not in currentList:
                result += solveBF(temp, currentList)
                currentList.append(temp)
    return result

# divides a string into substrings
# that start with 1 and end with 0
# with 0's and 1's separated
def divideString(currentString):
    if not len(currentString): return []

    indexForZero = currentString.index('0')
    if '1' not in currentString[indexForZero+1:]: return [currentString]

    indexForOne = currentString[indexForZero+1:].index('1')
    return [currentString[:indexForZero+1+indexForOne]] + divideString(currentString[indexForZero+1+indexForOne:])

def solve(myString):
    substrings = divideString(myString)
    result = solveBF(substrings[-1], [])

    for i in reversed(range(len(substrings)-1)):
        tempResult0 = solveBF(substrings[i]+'0', [])
        tempResult1 = solveBF(substrings[i], [])

        tempResult = np.array([tempResult0, tempResult1])
        tempResult = tempResult.transpose()

        result = sum((result*tempResult).transpose())

    return result

num = 5**25
string = bin(num)[2:] + '0'*25
#string = '1010'
result = solve(string)
print(sum(result))
