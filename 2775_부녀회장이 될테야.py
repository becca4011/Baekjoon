import math

T = int(input())

for i in range(T):
    floor = int(input())
    unit = int(input())

    num = math.factorial(unit + floor) // (math.factorial(unit - 1) * math.factorial(floor + 1))

    print(num)