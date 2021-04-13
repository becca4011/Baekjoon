import sys

def fibo(n):
    zero = [1, 0]
    one = [0, 1]

    if n <= 1:
        return
    for x in range(2, n + 1):
        zero.append(zero[x - 1] + zero[x - 2])
        one.append(one[x - 1] + one[x - 2])

    return zero, one

T = int(sys.stdin.readline())
zero, one = fibo(40)

for i in range(T):
    N = int(sys.stdin.readline())
    print(zero[N], one[N])

"""
fibo = [0]
for x in range(1, 10):
    if x < 2:
        fibo.append(1)
    else:
        fibo.append(fibo[x - 2] + fibo[x - 1])

print(fibo)
"""