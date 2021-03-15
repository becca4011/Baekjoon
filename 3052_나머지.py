import sys

li = []

for i in range(10):
    n = int(sys.stdin.readline())
    li.append(n % 42) # 42로 나눈 값 저장

set = set(li) # set은 중복된 값을 제거하면 나머지가 다른 것만 남음
print(len(set)) # set의 length를 출력하면 나머지가 다른 것의 수를 출력하는 것과 같음