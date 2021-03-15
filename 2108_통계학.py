from collections import Counter
import sys

li = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    num = sys.stdin.readline().rstrip()
    li.append(int(num))

li.sort()

avg = round(sum(li) / n) # round : 반올림
cen = li[n // 2]
mod = Counter(li)
mod = mod.most_common(n)
mode = mod[0][0]
if n != 1 and mod[0][1] == mod[1][1]:
    for i in range(n):
        if mod[i][1] == mod[i+1][1]:
            mode = mod[i+1][0]
            break
ran = max(li) - min(li)

print(avg)
print(cen)
print(mode)
print(ran)
