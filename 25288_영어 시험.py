import sys

N = int(sys.stdin.readline())
ans = sys.stdin.readline().rstrip()
r_ans = ans[::-1]
print(r_ans + ans)