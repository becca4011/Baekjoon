import sys

N, C = map(int, sys.stdin.readline().split())
msg = list(map(int, sys.stdin.readline().split()))

freq = dict()
for i in range(len(msg)):
    freq[msg[i]] = freq.get(msg[i], 0) + 1

freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
for i in freq:
    print((str(i[0]) + " ") * i[1], end="")
