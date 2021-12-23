import sys

while True:
    st = sys.stdin.readline().rstrip()
    if st == "*":
        break

    res = 0
    for i in range(len(st) - 1):
        dt = dict()
        for j in range(i + 1, len(st)):
            dt[st[j - i - 1] + st[j]] = dt.get(st[j - i - 1] + st[j], 0) + 1
            if dt[st[j - i - 1] + st[j]] > 1:
                res = 1

    if res == 0:
        print(st + " is surprising.")
    else:
        print(st + " is NOT surprising.")
