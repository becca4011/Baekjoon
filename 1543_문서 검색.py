import sys

text = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

cnt = 0
while text.find(word) != -1:  # 찾을 수 없으면 -1이 나옴
    n = text.find(word)
    text = text[n + len(word) :]
    cnt += 1

print(cnt)
