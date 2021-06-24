import sys

def cal(a, b):
    if b == 1:
        return a % c
    else:
        d = cal(a, b // 2) # 분할정복
        if b % 2 == 0:
            return d * d % c
        else:
            return d * d * a % c # 홀수인 경우 계산한 값에 a를 곱해야 함 (a^11이면 a^5 * a^2 * a를 해야 11)

a, b, c = map(int, sys.stdin.readline().split())
print(cal(a, b))