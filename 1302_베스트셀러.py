import sys

N = int(sys.stdin.readline())
books = dict()

for i in range(N):
    b = sys.stdin.readline().rstrip()
    books[b] = books.get(b, 0) + 1

books = sorted(books.items(), key=(lambda x: (-x[1], x[0])))  # -를 붙이면 내림차순
print(books[0][0])
