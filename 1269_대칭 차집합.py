import sys

a, b = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

print(len(set(A) - set(B)) + len(set(B) - set(A)))
