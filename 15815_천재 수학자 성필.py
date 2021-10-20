import sys

mt = sys.stdin.readline().rstrip()
li = list()

for i in mt:
    try:
        li.append(int(i))
    except:
        a = li.pop()
        b = li.pop()
        res = 0
        if i == "+":
            res = a + b
        elif i == "-":
            res = b - a  # 순서
        elif i == "*":
            res = a * b
        elif i == "/":
            res = b // a  # 순서
        li.append(res)

print(li[0])
