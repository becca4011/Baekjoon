import sys

n = int(sys.stdin.readline())
nums = sys.stdin.readline().split()
inums = list(map(int, nums))
print(min(inums), max(inums))