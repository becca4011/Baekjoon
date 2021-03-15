import sys

cnt = sys.stdin.readline().rstrip()
num = sys.stdin.readline()
sum = 0

for i in range(int(cnt)):
    sum += int(num[0:1])
    num = num[1:]

print(sum)
