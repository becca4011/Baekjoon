import sys
import math

A, B = map(int, sys.stdin.readline().split())
A, B = min(A, B), max(A, B)
print("1" * math.gcd(A, B))
