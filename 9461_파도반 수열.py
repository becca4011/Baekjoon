import sys

T = int(sys.stdin.readline())
dp = [1, 1, 1] + [0] * 97

for i in range(3, len(dp)):
    dp[i] = dp[i - 3] + dp[i - 2]

for i in range(T):
    N = int(sys.stdin.readline())
    print(dp[N - 1])
