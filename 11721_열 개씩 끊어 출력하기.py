import sys

st = sys.stdin.readline().rstrip()

cnt = 0
for s in st:
    if cnt < 9:
        print(s, end = "")
        cnt += 1
    else:
        print(s)
        cnt = 0
