import sys

T = int(sys.stdin.readline())
for i in range(T):
    y, m = map(int, sys.stdin.readline().split())
    m -= 1
    d = 0
    if m == 0:
        m = 12
        y -= 1
    
    if m in [1, 3, 5, 7, 8, 10, 12]:
        d = 31
    elif m in [4, 6, 9, 11]:
        d = 30
    else:
        if y % 100 != 0 and y % 4 == 0 or y % 400 == 0:
            d = 29
        else:
            d = 28
    
    print(y, m, d)