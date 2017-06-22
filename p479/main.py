M=10**9+7
N=10**6
def f(k):
    return ((pow(1-k*k,N+1,M)-1)*pow(-k*k,M-2,M)-1)%M

print(sum(f(k) for k in range(1,N+1))%M)
