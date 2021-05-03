import sys

N, M = map(int, sys.stdin.readline().split())
password = dict()

for i in range(N):
    site, pw = sys.stdin.readline().split()
    password[site] = pw

for i in range(M):
    print(password[sys.stdin.readline().rstrip()])