import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dq = deque(_ for _ in range(1, N + 1))
pop_li = list(map(int, sys.stdin.readline().split()))

cnt = 0
res_cnt = 0
while len(pop_li) != res_cnt:
    if dq[0] == pop_li[res_cnt]:
        dq.popleft()
        res_cnt += 1
    else:
        if dq.index(pop_li[res_cnt]) <= ((N - res_cnt) // 2):
            dq.append(dq.popleft())
            cnt += 1
        else:
            dq.appendleft(dq.pop())
            cnt += 1

print(cnt)
