from math import log

base = 3
numForEach = base * (base + 1) // 2

def solve(height):
    if height == 0: return 0

    bigLimit = int( log(height, base) )
    if bigLimit > 0:
        result = numForEach ** bigLimit
        return result + 2 * solve( height - (base ** bigLimit) )

    return height * (height + 1) // 2

def newSolve(height):
    result = 0
    branchNum = 1
    while height > 0:
        bigLimit = int( log(height, base) )

        if bigLimit > 0:
            result += branchNum * (numForEach ** bigLimit)
            branchNum += 1
            height -= base ** bigLimit

        else:
            result += branchNum * height * (height + 1) // 2
            break

    return result

totalHeight = 9
print( newSolve(totalHeight) )
