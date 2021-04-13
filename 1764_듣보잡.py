import sys

N, M = map(int, sys.stdin.readline().split())

lsn = set()
see = set()

for i in range(N):
    lsn.add(sys.stdin.readline().rstrip())

for i in range(M):
    see.add(sys.stdin.readline().rstrip())

ls = sorted(list(lsn & see))

print(len(ls))
for i in ls:
    print(i)