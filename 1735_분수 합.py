from math import gcd
import sys

x1, x2 = map(int, sys.stdin.readline().rstrip().split(' '))
y1, y2 = map(int, sys.stdin.readline().rstrip().split(' '))

n = gcd(x1*y2 + y1*x2, x2*y2)
print((x1*y2 + y1*x2) // n, (x2*y2) // n)

# 분수를 더했을 때의 분자, 분모
# 분자 : x1*y2 + x2*y1
# 분모 : x2*y2
# 기약분수로 만들기 위해서는 분자와 분모의 최대공약수(gcd)로 나누어주면 된다.
