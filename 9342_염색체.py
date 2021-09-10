import sys
import re

T = int(sys.stdin.readline())
cp = re.compile("^[A-F]?A+F+C+[A-F]?$")

for i in range(T):
    st = sys.stdin.readline()
    res = cp.match(st)

    if res == None:
        print("Good")
    else:
        print("Infected!")
