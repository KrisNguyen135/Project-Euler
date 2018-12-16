from math import sqrt

score1 = {'0':12, '1':4, '2':10, '3':10, '4':8, '5':10, '6':12, '7':8, '8':14, '9':12}
score2 = {'00':0, '01':4, '02':3, '03':3, '04':4, '05':3, '06':2, '07':2, '08':1, '09':2,
                  '11':0, '12':5, '13':3, '14':2, '15':5, '16':6, '17':2, '18':5, '19':4,
                          '22':0, '23':2, '24':5, '25':4, '26':3, '27':5, '28':2, '29':3,
                                  '33':0, '34':3, '35':2, '36':1, '37':3, '38':2, '39':1,
                                          '44':0, '45':3, '46':4, '47':2, '48':3, '49':2,
                                                  '55':0, '56':1, '57':3, '58':2, '59':1,
                                                          '66':0, '67':4, '68':1, '69':2,
                                                                  '77':0, '78':3, '79':2,
                                                                          '88':0, '89':1,
                                                                                  '99':0}

def getPrimes(lower, upper):
    sieve = [True] * upper
    newLimit = int(sqrt(upper)) + 1
    for i in range(2, newLimit):
        if sieve[i]:
            for j in range(i * 2, upper, i):
                sieve[j] = False
    return [i for i in range(lower, upper) if sieve[i]]

def getSequence(num, tempSequence):
    if num < 10: return tempSequence
    string = str(num)
    result = sum(int(char) for char in string)
    return getSequence(result, tempSequence + [result])

def getScore1(sequence):
    return sum(sum(score1[char] for char in str(num)) for num in sequence)

def getScore2(sequence):
    result = sum(score1[char] for char in str(sequence[0])) // 2
    for i in range(len(sequence) - 1):
        num1 = str(sequence[i])
        num2 = str(sequence[i + 1])
        offset = len(num1) - len(num2)
        result += sum(score1[char] for char in num1[:offset]) // 2
        #result += sum(score2[min(num1[offset + j], num2[j]) + max(num1[offset + j], num2[j])] for j in range(len(num2)))
        for j in range(len(num2)):
            char1 = num1[offset + j]
            char2 = num2[j]
            result += score2[min(char1, char2) + max(char1, char2)]
    result += sum(score1[char] for char in str(sequence[-1])) // 2
    return result

#sequence = getSequence(137, [137])
#print(sequence)
#print(getScore2(sequence))
primes = getPrimes(0, 2000000)
result = 0
for prime in primes:
    print(prime)
    sequence = getSequence(prime, [prime])
    result += getScore1(sequence)
    result -= getScore2(sequence)
print(result)
