import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    text = "".join(sys.stdin.readline().rstrip().split()).upper()
    dt = dict()

    i = 0
    m = 0
    cnt = 0
    while True:
        if len(dt) == len(text):
            break
        if i >= len(text):
            cnt += 1
            i = cnt
        dt[i] = text[m]
        i += N
        m += 1
    dt = sorted(dt.items(), key=lambda x: x[0])
    for i in dt:
        print(i[1], end="")
    print()
