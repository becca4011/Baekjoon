import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))
btn = [str(x) for x in range(10) if x not in broken] # 부서진 버튼 제외한 버튼

min_ch = abs(100 - N) # 원래 채널에서 +/-로만 채널 맞추는 경우

# 가까운 채널로 이동한 후 +/-로 채널 맞추는 경우
# 500000 채널까지 존재하기 때문에 500000 보다 크면서 모든 숫자의 경우를 거치는 1000000까지를 범위로 잡아야 함
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in btn:
            break
        elif j == len(num) - 1:
            min_ch = min(min_ch, abs(N - int(num)) + len(str(num)))

print(min_ch)