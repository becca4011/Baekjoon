r = ''
res = []
n = int(input())
for i in range(n):
    cnt, st = input().split(' ')
    for s in st:
        r += s * int(cnt)
    res.append(r)
    r = ''

for i in range(n):
    print(res[i])
