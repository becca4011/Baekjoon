import sys

eng = {}
for e in range(26):
    eng[chr(65 + e)] = 0

st = sys.stdin.readline().rstrip().upper()

for s in st:
    eng[s] += 1

max = 0
for key, value in eng.items():
    if value != 0 and max < value:
        max = value

cnt = 0
res = ""
for key, value in eng.items():
    if value == max:
        cnt += 1
        res = key

if cnt == 1:
    print(res)
else:
    print("?")
