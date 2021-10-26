import sys

N, K = map(int, sys.stdin.readline().split())
li = list()

for i in range(N):
    li.append(float(sys.stdin.readline().rstrip()) * 10)

li.sort()
t_mean = sum(li[K : N - K]) / (N - K * 2) / 10
for i in range(K):
    li[i] = li[K]
for i in range(K):
    li[N - i - 1] = li[N - K - 1]
a_mean = sum(li) / N / 10

print("{:.2f}".format(t_mean + 0.00000001))
print("{:.2f}".format(a_mean + 0.00000001))
