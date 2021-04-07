import  sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)
res = 0
while (start <= end):
    mid = (start + end) // 2

    cnt = sum(t - mid if mid < t else 0 for t in tree) # 시간초과 해결

    if cnt < M:
        end = mid - 1
    elif cnt >= M:
        start = mid + 1
        res = mid # 최댓값 찾기

print(res)