from math import gcd
import sys

def lcm(x, y):
    return x * y // gcd(x, y) # 최대공약수로 최소공배수 구하기

num = sys.stdin.readline().rstrip()

for i in range(int(num)):
    x, y = input().split()
    x = int(x)
    y = int(y)
    print(lcm(x, y))
