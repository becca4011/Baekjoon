import sys

stack = []
res = 1

while True:
    st = sys.stdin.readline().rstrip()
    if st == '.':
        break

    for s in st:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                res = 0
                break
        elif s == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                res = 0
                break

    if res == 0:
        print("No")
    else:
        print("Yes")

