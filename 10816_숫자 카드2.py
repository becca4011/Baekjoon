import sys

N = int(sys.stdin.readline())
Nnum = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mnum = map(int, sys.stdin.readline().split()) # list 쓰고, 조건문 걸었는데 시간초과

def binary(left, right, find):
    if left > right:
        return 0

    mid = (left + right) // 2
    if Nnum[mid] == find:
        return Nnum[left:right+1].count(find)
    elif Nnum[mid] < find:
        return binary(mid + 1, right, find)
    elif Nnum[mid] > find:
        return binary(left, mid - 1, find)

dic = {}
for find in Nnum:
    if find not in dic:
        dic[find] = binary(0, N - 1, find)

for i in Mnum:
    if i in dic:
        print(dic[i], end=" ") # Mnum에 있으면 수 출력
    else:
        print(0, end=" ") # 없으면 0 출력