import sys

vidio = list()

def check(row, col, size):
    p = vidio[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if p != vidio[i][j]:
                print("(", end="")
                return False
    return True

def partition(row, col, size):
    if check(row, col, size):
        if vidio[row][col] == '0':
            print(0, end="")
        elif vidio[row][col] == '1':
            print(1, end="")
        return

    new_size = size // 2
    partition(row, col, new_size)
    partition(row, col + new_size, new_size)
    partition(row + new_size, col, new_size)
    partition(row + new_size, col + new_size, new_size)
    
    print(")", end="")

N = int(sys.stdin.readline())
for i in range(N):
    vidio.append(list(sys.stdin.readline().rstrip()))

partition(0, 0, N)