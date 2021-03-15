import sys

stack = []

num = sys.stdin.readline().rstrip()
for i in range(int(num)):
    s = int(sys.stdin.readline().rstrip())
    if s == 0:
        stack.pop();
    else:
        stack.append(s);

print(sum(stack))
