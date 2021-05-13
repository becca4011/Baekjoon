import sys

colored_paper = list()
white = 0
blue = 0

# 색이 같은지 검사
def check(row, col, size):
    color = colored_paper[row][col] # 색종이의 첫 번째 칸

    for i in range(row, row + size):
        for j in range(col, col + size):
            if color != colored_paper[i][j]: # 검사했을 때 같지 않으면 색종이를 잘라야 하므로 False 리턴
                return False

    return True # 아무 조겐에 걸리지 않으면 True 리턴 (색종이를 더 이상 자르지 않아도 됨)

# 색종이 자르기
def partition(row, col, size):
    global white, blue # UnboundLocalError 방지
    if check(row, col, size): # 색이 같은지 검사
        if colored_paper[row][col] == 0: # 0이면 흰색
            white += 1
        else:
            blue += 1
        return

    new_size = size // 2 # 자르기 (1/2씩 자름)

    # 재귀
    partition(row, col, new_size)
    partition(row, col + new_size, new_size)
    partition(row + new_size, col, new_size)
    partition(row + new_size, col + new_size, new_size)
    

N = int(sys.stdin.readline())

for i in range(N):
    colored_paper.append(list(map(int, sys.stdin.readline().split())))

partition(0, 0, N)

print(white)
print(blue)