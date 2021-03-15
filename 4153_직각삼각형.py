while(1):
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break

    line = [x, y, z]
    line = sorted(line)
    
    if line[0] ** 2 + line[1] ** 2 == line[2] ** 2:
        print("right")
    else:
        print("wrong")