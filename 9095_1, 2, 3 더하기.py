import sys

dp = [1, 2, 4] + [0] * 8

for i in range(3, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

T = int(sys.stdin.readline())
for i in range(T):
    print(dp[int(sys.stdin.readline()) - 1])