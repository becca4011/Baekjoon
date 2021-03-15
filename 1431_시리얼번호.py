def intsum(x):
    sum = 0;
    for i in x:
        if i.isdigit():
            sum += int(i)
    return sum

num = int(input());
arr = [];
for i in range(num):
    arr.append(input())

arr.sort(key = lambda x: (len(x), intsum(x), x)) # 길이, 숫자합, 사전순 정렬

for i in range(len(arr)):
    print(arr[i])
