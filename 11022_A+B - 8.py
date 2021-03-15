import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = sys.stdin.readline().split()
    print(f"Case #{i+1}: {a} + {b} = {int(a) + int(b)}")