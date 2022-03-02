import sys

N = int(sys.stdin.readline())

li = list()
for i in range(N):
    word = sys.stdin.readline().rstrip()
    
    k = 1
    s = ""
    dt = dict()
    
    for j in range(26):
        dt[chr(j + 97)] = -1;

    dt[word[0]] = 1
    for j in range(len(word)):
        if j != 0 and dt[word[j]] == -1:
            k += 1
            dt[word[j]] = k
            s += str(k)
        else:
            s += str(dt[word[j]])
        
    li.append(s)
    
res = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if li[i] == li[j]:
            res += 1

print(res)