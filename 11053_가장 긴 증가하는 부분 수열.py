import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
num = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i] and num[i] < num[j] + 1:
            num[i] = num[j] + 1
            #print(num)
            
print(max(num))