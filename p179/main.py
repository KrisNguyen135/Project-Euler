L = 10**7

n = [0]*(L)
for i in range(2, L//2):
    print(i)
    for j in range(i*2, L, i):
        n[j] += 1

print("Consecutive divisors =", sum(n[i] == n[i - 1] for i in range(3, L)))
