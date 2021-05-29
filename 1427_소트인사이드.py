import sys

N = sorted(list(sys.stdin.readline().rstrip()), reverse=True)
print(''.join(N))