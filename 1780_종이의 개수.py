import sys

paper = list()
m_one = 0
zero = 0
one = 0

def check(row, col, size):
    num = paper[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if num != paper[i][j]:
                return False
    return True

def partition(row, col, size):
    global m_one, zero, one

    if check(row, col, size):
        if paper[row][col] == -1:
            m_one += 1
        elif paper[row][col] == 0:
            zero += 1
        elif paper[row][col] == 1:
            one += 1
        return
        
    new_size = size // 3
    partition(row, col, new_size)
    partition(row, col + new_size, new_size)
    partition(row, col + new_size * 2, new_size)
    partition(row + new_size, col, new_size)
    partition(row + new_size, col + new_size, new_size)
    partition(row + new_size, col + new_size * 2, new_size)
    partition(row + new_size * 2, col, new_size)
    partition(row + new_size * 2, col + new_size, new_size)
    partition(row + new_size * 2, col + new_size * 2, new_size)

N = int(sys.stdin.readline())

for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

partition(0, 0, N)
print(m_one)
print(zero)
print(one)