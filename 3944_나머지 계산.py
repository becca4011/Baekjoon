import sys

T = int(sys.stdin.readline())

res = list()
for i in range(T):
    B, D = sys.stdin.readline().split()
    D = sum(list(map(int, str(D))))
    print(D % (int(B) - 1))