import sys

chess_white = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

chess_black = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

N, M = map(int, sys.stdin.readline().split())

def chess_check(chess):
    cnt_white = 0
    cnt_black = 0

    for i in range(8):
        # 흰색이 먼저 나오는 체스판 검사
        if chess[i] != chess_white[i]:
            for c in range(len(chess[i])):
                if chess[i][c] != chess_white[i][c]:
                    cnt_white += 1

        # 검은색이 먼저 나오는 체스판 검사
        if chess[i] != chess_black[i]:
            for c in range(len(chess[i])):
                if chess[i][c] != chess_black[i][c]:
                    cnt_black += 1

    return cnt_white if cnt_white < cnt_black else cnt_black

# 체스판 넣기
chess = list()
for i in range(N):
    chess.append(input())

cut_chess = list()
cnt = list()
for i in range(N - 7):
    for j in range(M):
        for k in range(i, i+8):
            if len(chess[k][j:j+8]) == 8:
                cut_chess.append(chess[k][j:j+8])
                if len(cut_chess) == 8:
                    cnt.append(chess_check(cut_chess))
                    cut_chess = []

print(min(cnt))

# 체스판이 8*8 보다 클 경우, 모두 8*8로 잘라서 가장 작은 카운트를 출력