""" Tabulation vs Memoization """


""" Memoization (Top-Down) """
def fib_memo(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    
    memo[n] = fib_memo(n-1,memo)+fib_memo(n-2,memo)
    return memo[n]

print(fib_memo(4))


""" Tabulation example """
def fib_tab(n):
    if n<=1:
        return n
    
    table = [0]*(n+1)
    table[1]=1
    table[0]=0

    for i in range(2,n+1):
        # table[2]=table[1]+table[0]
        table[i]=table[i-1]+table[i-2]
    return table[n]

print(fib_tab(4))


# LRU caching
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(4))