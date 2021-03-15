N = int(input())
res = 0

for i in range(N):
    word = input()

    for j in range(len(word)):
        if j != len(word) - 1:
            if word[j] == word[j + 1]: # 앞 뒤가 같은 문자
                continue # 넘어감
            elif word[j] in word[j + 1:]: # 앞 문자가 뒤의 문자열 안에 있는지 검사
                break # for문 빠져나감
        else:
            res = res + 1 # 위 break에서 걸리지 않으면 1 증가

print(res)