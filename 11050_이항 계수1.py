"""
import math

N, K = map(int, input().split())
print(math.factorial(N)//(math.factorial(K)*math.factorial(N - K)))
"""

def fact(i):
    mul = 1
    for j in range(i):
        mul *= j + 1
    return mul

N, K = map(int, input().split())

print(fact(N)//(fact(K)*fact(N - K)))