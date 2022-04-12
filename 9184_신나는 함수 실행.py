import sys

li = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        if li[20][20][20] == 0:
            li[20][20][20] = w(20, 20, 20)
        return li[20][20][20]
    elif a < b and b < c:
        if li[a][b][c] == 0:
            li[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return li[a][b][c]
    else:
        if li[a][b][c] == 0:
            li[a][b][c] =  w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return li[a][b][c]
    

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))