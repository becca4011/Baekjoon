import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    one = list(map(str, sys.stdin.readline().split()))
    two = list(map(str, sys.stdin.readline().split()))
    pw = list(map(str, sys.stdin.readline().split()))

    li = list()
    for j in range(n):
        li.append(
            pw[two.index(one[j])]
        )  # one에 대한 two의 index가 나오는데, 이 순서로 list에 넣으면 평문이 나옴
    print(" ".join(li))
