import sys

N = int(sys.stdin.readline())
post = list(sys.stdin.readline().rstrip())

li = list()
for i in range(N):
    li.append(int(sys.stdin.readline()))

stack = list()
for p in post:
    if p == "+" or p == "-" or p == "*" or p == "/":
        a = stack.pop()
        b = stack.pop()
        if p == "+":
            stack.append(a + b)
        elif p == "-":
            stack.append(b - a)
        elif p == "*":
            stack.append(b * a)
        elif p == "/":
            stack.append(b / a)
    else:
        stack.append(li[ord(p) - ord("A")])

print("{:.2f}".format(round(stack[0], 2)))
