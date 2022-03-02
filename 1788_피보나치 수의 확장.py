import sys

def fibo(n):
    dt = {-1: 1, 0: 0, 1: 1}
    dt[n] = fibo(dt[n - 1]) + fibo(dt[n - 2])
    # dt[1] = dt[0] + dt[-1]
    # dt[0] = dt[-1] + dt[-2]
    # dt[-1] = dt[-2] + dt[-3]
    # dt[-2] = dt[-3] + dt[-4]

N = int(sys.stdin.readline())
res = fibo(N)
if res < 0:
    print(-1)
elif res == 0:
    print(0)
else:
    print(1)
print(abs(res) % 1000000000)