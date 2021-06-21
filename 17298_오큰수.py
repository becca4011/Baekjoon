import sys
from collections import deque

# 이중 for문은 시간 초과
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

stack = deque()
res = [-1] * N

for i in range(N):
    while len(stack) != 0 and stack[-1][0] < A[i]: # 스택이 비어있지 않고, 비교했을 때 A[i]가 더 큰 경우
        item, index = stack.pop() # 스택에서 빼기
        res[index] = A[i] # 오큰수를 res에 저장 (index를 같이 저장하면 해당 인덱스의 오큰수를 알 수 있음)
    stack.append([A[i], i]) # 아이템, 인덱스 같이 저장

for i in range(len(res)):
    print(res[i], end=" ")