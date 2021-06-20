# 시간초과
n = int(input())

def star(i, j, n):
    if (i // n) % 3 == 1 and (j // n) % 3 == 1: # j가 2, 4, 6, 8, ...
        print(" ", end = "")
    else:
        if n // 3 == 0:
            print("*", end = "")
        else:
            star(i, j, n // 3) # n을 3 나눠서 다시 돌림

for i in range(n):
    for j in range(n):
        star(i, j, n)
    print()