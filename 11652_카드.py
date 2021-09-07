import sys

N = int(sys.stdin.readline())
card = dict()

for i in range(N):
    card_num = int(sys.stdin.readline())
    card[card_num] = card.get(card_num, 0) + 1

card = sorted(card.items(), key=(lambda x: (-x[1], x[0])))
print(card[0][0])
