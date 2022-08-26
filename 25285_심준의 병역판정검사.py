import sys

T = int(sys.stdin.readline())
for i in range(T):
    cm, kg = map(int, sys.stdin.readline().split())
    bmi = kg / ((cm / 100) ** 2)
    
    if cm < 140.1:
        print(6)
    elif cm < 146:
        print(5)
    elif cm < 159:
        print(4)
    elif cm < 161:
        if bmi >= 16.0 and bmi < 35.0:
            print(3)
        else:
            print(4)
    elif cm < 204:
        if bmi >= 20.0 and bmi < 25.0:
            print(1)
        elif bmi >= 18.5 and bmi < 30.0:
            print(2)
        elif bmi >= 16.0 and bmi < 35.0:
            print(3)
        else:
            print(4)
    else:
        print(4)