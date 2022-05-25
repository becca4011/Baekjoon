import sys

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

if P in S:
    print(1)
else:
    print(0)