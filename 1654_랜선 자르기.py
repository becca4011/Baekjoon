import sys

K, N = map(int, sys.stdin.readline().split())

lan = list()
for i in range(K):
    lan.append(int(input()))

start = 1
end = max(lan)
while(start <= end):
    sum = 0 # 랜선의 개수
    mid = (start + end) // 2 # start와 end의 값을 더하고 2로 나눔

    for l in lan:
        sum += l // mid # 랜선이 얼마나 나오는지 계산 (804 // 200 = 4개)

    if sum >= N: # 필요한 랜선보다 더 많이 나오는 경우
        start = mid + 1 # start를 mid + 1로 바꾸기 (랜선 길이를 더 늘림)
    elif sum <= N: # 필요한 랜선보다 더 적게 나오는 경우
        end = mid - 1 # end를 mid - 1로 바꾸기 (랜선 길이를 더 줄임)

print(end) # end가 랜선의 최대 길이