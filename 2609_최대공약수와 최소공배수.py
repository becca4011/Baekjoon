"""
# math 사용
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(a // math.gcd(a, b) * b)
"""

# 유클리드 호제법
def gcd(n, m):
    while (m != 0):
        n, m = m, n % m
    return n

a, b = map(int, input().split())

print(gcd(a, b))
print(a // gcd(a, b) * b)


"""
<유클리드 호제법>
24 18

24는 18로 나누어떨어지지 않음 → 24 % 18 = 6
18은 6으로 나누어떨어짐 → 최대공약수 = 6
"""