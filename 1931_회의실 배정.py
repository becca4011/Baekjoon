import sys

N = int(sys.stdin.readline())
meeting = list()

for i in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))

meeting.sort(key = lambda x: (x[1], x[0]))

end = meeting[0][1]
cnt = 1
for i in range(1, N):
    if end <= meeting[i][0]:
        cnt += 1
        end = meeting[i][1]

print(cnt)