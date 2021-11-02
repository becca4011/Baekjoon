import sys
from typing import Counter

N = int(sys.stdin.readline())

shortcut = list()
res = list()
for i in range(N):
    st = sys.stdin.readline().rstrip()
    st_split = st.split()

    for j in range(len(st_split)):
        if st_split[j] != " " and st_split[j][0].upper() not in shortcut:
            shortcut.append(st_split[j][0].upper())
            st_split[j] = "[" + st_split[j][0] + "]" + st_split[j][1:]
            res.append("".join(st_split))
            break

    else:
        for j in range(len(st)):
            if st[j].upper() not in shortcut and st[j] != " ":
                shortcut.append(st[j].upper())
                st = st[:j] + "[" + st[j] + "]" + st[j + 1 :]
                res.append("".join(st))
                break
        else:
            res.append(st)

for i in res:
    print(i)
