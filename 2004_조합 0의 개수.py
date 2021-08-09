import sys


def div(num, k):
    i = k
    cnt = 0
    while num + 1 > i:
        cnt += num // i
        i = i * k
    return cnt


n, m = map(int, sys.stdin.readline().split())

# 뒤 0의 개수는 2, 5의 개수에 따라 결정 (2 * 5 = 10 이므로 둘 중 적게 나온 수가 정답)
print(min(div(n, 5) - div(m, 5) - div(n - m, 5), div(n, 2) - div(m, 2) - div(n - m, 2)))
