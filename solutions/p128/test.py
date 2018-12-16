primelist = [2, 3]

primeslist = dict()

for i in primelist:
    primeslist[i] = 1

def isprime(x):
    x = abs(x)
    i = primelist[-1]
    while (primelist[-1] < x):
        i += 2
        flag = True
        j = 0
        while j < len(primelist):
            if i % primelist[j] == 0 or primelist[j] ** 2 > i:
                if i % primelist[j] == 0:
                    flag = False
                j = len(primelist)
            j += 1
        if flag == True:
            primelist.append(i)
            primeslist[i] = 1
    #return primeslist.has_key(x)
    return x in primeslist

m = 100
r = [1]
n = 1

while len(r) < m:
	if isprime((6 * n + 1)) and isprime((6 * n - 1)) and isprime((12 * n + 5)):
		r.append(3 * n * (n-1) + 2)
	if isprime((6 * n + 5)) and isprime((6 * n - 1)) and isprime((12 * n - 7)) and n != 1:
		r.append(3 * n * (n + 1) + 1)
	n += 1
print(r[-1])
