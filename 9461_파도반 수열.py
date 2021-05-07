import sys

T = int(sys.stdin.readline())
dp = [1, 1, 1] + [0] * 97 # list 생성 (100개)

for i in range(3, len(dp)):
    dp[i] = dp[i - 3] + dp[i - 2] # 점화식

for i in range(T):
    N = int(sys.stdin.readline())
    print(dp[N - 1])
