import sys
from itertools import permutations

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, sys.stdin.readline().split())

st = "+ " * plus + "- " * minus + "* " * mul + "// " * div
li = st.split()
test = set(permutations(li, len(li)))

res = list()
for i in test:
    sum = A[0]
    for j in range(len(i)):
        if i[j] == "+":
            sum += A[j + 1]
        elif i[j] == "-":
            sum -= A[j + 1]
        elif i[j] == "*":
            sum *= A[j + 1]
        elif i[j] == "//":
            if sum < 0:
                sum = -(abs(sum) // A[j + 1])
            else:
                sum //= A[j + 1]
    res.append(sum)

print(max(res), min(res))