#fibonaci sequence
'''
fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n==1 or n==2:
        value = 1
    if n>2:
        value = fibonacci(n-1)+fibonacci(n-2)
        
    fibonacci_cache[n]= value
    return value
print(fibonacci_cache)
'''
#method 2
from functools import lru_cache
import time

@lru_cache(maxsize= 500)
def fibonacci(n):
    #check that the input is a positive integer
    if type(n) != int:
        raise TypeError(' n must be a positive int')
    if n < 1:
        raise TypeError(' n must be a positive int')
    if n ==1 or n==2:
        return 1
    if n>2:
        return fibonacci(n-1) + fibonacci(n-2)
t0 = time.time()
for i in range(1, 21):
    print(i, ':', fibonacci(i))
t1 = time.time()

print('time required', t1-t0)
a = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]

def sum1(n):
    if n==0:
        return 0
    return n+ sum1(n-1)
#tinh gcd
def gcd(a, b):
    if a*b ==0:
        return a + b
    if a>b:
        return gcd(a%b, b)
    return gcd(a, b%a)
print(gcd(12, 16))



















