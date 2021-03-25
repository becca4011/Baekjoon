import sys
from collections import deque 

# queue를 사용하면 시간 초과 (데이터 추가/삭제 : O(1), 데이터 접근 : O(N))
# deque를 사용하면 맞음 (메소드 모두 O(1))
# 시간복잡도에서 deque가 뛰어남 (시간이 2초, 추가시간이 없으므로 deque를 쓰자)

N = int(sys.stdin.readline())

q = deque()
for i in range(1, N+1):
    q.append(i)

while (len(q) > 2):
    q.popleft()
    q.append(q.popleft())

if len(q) == 1:
    print(q[0])
else:
    print(q[1])