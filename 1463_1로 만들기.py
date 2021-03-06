import sys

N = int(sys.stdin.readline())

# 점화식 : dp(N) = min(dp(N // 3) + 1, dp(N // 2) + 1, dp(N - 1) + 1)
dp = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
    elif i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

print(dp[N])