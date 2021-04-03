import sys

stack = []
res = 1

while True:
    st = sys.stdin.readline().rstrip()
    if st == '.':
        break

    for s in st:
        if s == ')' and len(stack) == 0 or s == ']' and len(stack) == 0:
            stack.append(s)
            break

        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')' and stack[-1] != '(':
            stack.append(s)
            break

        elif s == ']' and stack[-1] != '[':
            stack.append(s)
            break

        elif s == ')' or s == ']':
            stack.pop()

    if len(stack) == 0:
        print("yes")
    else:
        print("no")

    stack = []