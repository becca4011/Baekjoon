import sys

li = [[0 for _ in range(101)] for _ in range(101)]


def combination(n, m):
    for i in range(n + 1):
        for j in range(m + 1):
            if i == j or j == 0:
                li[i][j] = 1
            else:
                li[i][j] = li[i - 1][j - 1] + li[i - 1][j]  # 조합 공식
    return li[n][m]


n, m = map(int, sys.stdin.readline().split())
print(combination(n, m))
