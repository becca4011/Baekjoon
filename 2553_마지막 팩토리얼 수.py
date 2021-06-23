import sys
import math

n = int(sys.stdin.readline())
nf = str(math.factorial(n))
nf = nf.replace('0', '')
print(nf[-1])