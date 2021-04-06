import sys

T = int(input())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    check = list(0 for _ in range(N)) # N까지 0을 넣은 list

    check[M] = 1 # M에 1을 넣기 (찾을 위치)
    cnt = 0 # 몇 번째로 인쇄하는지
    while True:
        if queue[0] == max(queue): # 0번째가 queue의 가장 큰 값과 같을 경우
            cnt += 1 # 우선순위 올리기

            if check[0] != 1: # 체크하는 리스트의 가장 앞이 1이 아닌 경우
                queue.pop(0) # 둘 다 pop
                check.pop(0)
            else:
                print(cnt) # 출력
                break
        else:
            queue.append(queue.pop(0)) # 맨 앞의 수를 가장 뒤로 넘기기
            check.append(check.pop(0)) # 체크 리스트도 같이 넘겨주기 (자리 찾아야 하므로)

        #print(queue)
        #print(check)
        #print(cnt)
        #print()