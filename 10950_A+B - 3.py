import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = sys.stdin.readline().split()
    print(int(a) + int(b))