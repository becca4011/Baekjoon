import sys

T = int(sys.stdin.readline())
for i in range(T):
    li = list()
    res = 0
    money = 5 * (10 ** 6)
    while True:
        ground = int(sys.stdin.readline())
        if ground == 0:
            break
        li.append(ground)

    li.sort(reverse=True)
    for j in range(len(li)):
        res += 2 * (li[j] ** (j + 1))

    if money < res:
        print("Too expensive")
    else:
        print(res)
