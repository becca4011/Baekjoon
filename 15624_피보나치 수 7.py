import sys

fibo = [0, 1]
for i in range(2, 1000001):
    fibo.append((fibo[i - 1] + fibo[i - 2]) % 1000000007)

n = int(sys.stdin.readline())
print(fibo[n])
