# pypy 성공
import math

n = int(input())
dp = [0, 1] + [0] * n

for i in range(2, n + 1):
    if i == int(math.sqrt(i)) ** 2:
        dp[i] = 1
    else:
        dp[i] = i

if dp[n] != 1:
    for i in range(2, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

print(dp[n])