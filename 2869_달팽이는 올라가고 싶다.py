import sys
A, B, V = map(int, sys.stdin.readline().split())

# 시간 초과
"""
m = 0
day = 0
while (True):
    m += A
    day += 1
    if m >= Y:
        print(day)
        break
    if m != Y:
        m -= B
"""
"""
m = 0
day = 0
while (m + A < V):
    m += A - B
    day += 1

print(day + 1)
"""

# 식을 만들었기 때문에 결과 바로 나옴
day = (V - B) / (A - B)
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)