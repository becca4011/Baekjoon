import sys

N, M = map(int, sys.stdin.readline().split())

pokemon = dict()
pokemon_reverse = dict()

for i in range(N):
    p = sys.stdin.readline().rstrip()
    pokemon[i] = p
    pokemon_reverse[p] = i

for i in range(M):
    question = sys.stdin.readline().rstrip()

    if question in pokemon_reverse.keys():
        print(pokemon_reverse[question] + 1)
    else:
        print(pokemon[int(question) - 1])