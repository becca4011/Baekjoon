# push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop
# 1   , 2   , 3   , 4   ,    ,    , 5   , 6   ,    , 7   , 8   ,    ,    ,    ,    , 
#     ,     ,     ,     , 4  , 3  ,     ,     , 6  ,     ,     , 8  , 7  , 5  , 2  , 1

int_sequence = []
stack = []
stack_pop = []
comp = []

n = int(input())

for i in range(n):
    int_sequence.append(int(input()))

max = 0
cnt = 0
for i in range(n): 
    if max < int_sequence[i]:
        max = int_sequence[i]

    if i < n - 1 and max == n and int_sequence[i] < int_sequence[i+1]:
        break

    if len(stack) < int_sequence[i]:
        for j in range(len(stack), int_sequence[i]):
            stack.append(j + 1)
            stack_pop.append(j + 1)
            comp.append("+")

    if len(stack) >= int_sequence[i]:
        if stack_pop.pop() != int_sequence[i]:
            break
        comp.append("-")

    cnt += 1

if cnt != n:
    print("NO")
else:
    for c in comp:
        print(c)