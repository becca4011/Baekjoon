# push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop
# 1   , 2   , 3   , 4   ,    ,    , 5   , 6   ,    , 7   , 8   ,    ,    ,    ,    , 
#     ,     ,     ,     , 4  , 3  ,     ,     , 6  ,     ,     , 8  , 7  , 5  , 2  , 1

int_sequence = [] # 입력한 수열
stack = [] # 스택
stack_check = [] # 수열 확인할 스택
comp = [] # +, - 저장

n = int(input()) # 1~n 까지의 수

for i in range(n):
    int_sequence.append(int(input())) # 수열 입력

max = 0 # max값 찾기
cnt = 0 # 모두 수행했는지 체크
for i in range(n): 
    if max < int_sequence[i]:
        max = int_sequence[i]

    if i < n - 1 and max == n and int_sequence[i] < int_sequence[i+1]: # max값이 나온 상태에서, 현재 값이 다음 값보다 작으면 수열이 성립하지 않으므로 break
        break

    if len(stack) < int_sequence[i]: # 스택의 길이보다 입력한 수가 클 경우 (스택에 push하기)
        for j in range(len(stack), int_sequence[i]): # 스택의 길이 ~ 입력한 수 - 1 (스택에 들어가있는 수보다는 큰 수가 들어와야 하고, 입력한 수까지 들어가야 함)
            stack.append(j + 1)
            stack_check.append(j + 1) # stack에서 pop을 하여 검사할 것
            comp.append("+") # push는 +

    if len(stack) >= int_sequence[i]: # 스택의 길이보다 입력한 수가 작거나 같을 경우 (스택에서 pop하기)
        if stack_check.pop() != int_sequence[i]: # pop을 한 값이 입력한 값과 같지 않으면 수열이 성립하지 않으므로 break
            break
        comp.append("-") # pop은 -

    cnt += 1 # 모든 수행 후 +1

if cnt != n: # cnt가 n과 같지 않다면 반복 수행 도중에 break된 것
    print("NO") # 철자 주의
else:
    for c in comp:
        print(c)