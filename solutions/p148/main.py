from math import log

limit = 9
base = 3
numForEach = base * (base + 1) // 2

# finding the big grid
bigLimit = int( log(limit, base) )
result = numForEach ** bigLimit

# finding how many layers the big grid is repeated
layerNum = limit // bigLimit
result *= layerNum * (layerNum + 1) // 2

newLimit = limit - bigLimit * layerNum
