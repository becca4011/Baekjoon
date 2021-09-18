import sys

# 단순 round를 사용하면 틀리는 문제를 해결
# python의 round는 앞자리가 짝수면 버리고, 홀수면 올리는 방식
def round_new(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    li = list()
    for i in range(n):
        li.append(int(sys.stdin.readline()))

    li.sort()
    per = round_new(n * 0.15)
    s_li = li[per : n - per]
    print(round_new(sum(s_li) / len(s_li)))
