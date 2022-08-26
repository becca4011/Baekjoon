import sys

def sort_num(n, li, so):
    for j in range(n):
        if li[j] != so[j]:
            li[j] = n - li[j] + 1
    return li

T = int(sys.stdin.readline())
ans = list()
for i in range(T):
    N = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    save = li[:]
    
    so = [_ for _ in range(1, N + 1)]
    
    while li != so:
        li = sort_num(N, li, so)
        li_s = sorted(li)
        if li == li_s:
            ans.append("YES")
            break
        if li == save:
            ans.append("NO")
            break
    else:
        ans.append("YES")
        
for i in ans:
    print(i)