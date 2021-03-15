import sys

eng = {}
for e in range(26):
    eng[chr(97 + e)] = -1

st = sys.stdin.readline().rstrip()
cnt = 0
for s in st:
    if eng[s] == -1:
        eng[s] = cnt
    cnt += 1

for e in range(26):
    print(eng[chr(97 + e)], end = " ")
