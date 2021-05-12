import sys

n = int(sys.stdin.readline())
st = list()
for i in range(n):
    st.append(int(sys.stdin.readline()))

dp = [0] * n
# dp[n] = dp[n - 2] + st[n] 마지막 계단 + 전전 계단 최댓값
# dp[n] = dp[n - 3] + st[n - 1] + st[n] 마지막 계단 + 마지막 전 계단 + 전전전 계단 최댓값

dp[0] = st[0]
# n은 300 이하의 자연수이므로 1 or 2도 올 수 있으므로 IndexError 방지하기
if n > 1:
    dp[1] = max(st[0] + st[1], st[1])
if n > 2:
    dp[2] = max(st[0] + st[2], st[1] + st[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + st[i], dp[i - 3] + st[i - 1] + st[i])

print(dp[n - 1])