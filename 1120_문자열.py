import sys

A, B = sys.stdin.readline().split()

res = list()
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[j + i]:
            cnt += 1
    res.append(cnt)

print(min(res))
