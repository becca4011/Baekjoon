import sys

num = int(sys.stdin.readline().rstrip()) # input()보다 빠름
arr = [0] * 10001

for i in range(num):
    arr[int(sys.stdin.readline().rstrip())] += 1
    # 배열의 인덱스를 작성한 수로 하고, 그에 대한 값을 그 수를 적은 횟수로 함 (7을 2번 적으면 arr[7] = 2)

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

