import sys

while(True):
    try:
        a, b = sys.stdin.readline().split()
        print(int(a) + int(b))
        
    except:
        break