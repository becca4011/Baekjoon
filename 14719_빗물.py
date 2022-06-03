import sys

H, W = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, W - 1):
    left = max(block[:i]) # 왼쪽에서 가장 높은 블록
    right = max(block[i + 1:]) # 오른쪽에서 가장 높은 블록
    
    compare = min(left, right)

    if block[i] < compare:
        ans += compare - block[i]

print(ans)