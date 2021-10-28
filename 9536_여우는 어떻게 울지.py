import sys

T = int(sys.stdin.readline())

for i in range(T):
    sound = sys.stdin.readline().split()
    animal_sound = list()
    while True:
        animal = sys.stdin.readline().rstrip()
        if animal == "what does the fox say?":
            break
        else:
            animal_sound.append(animal.split()[2])

    fox = list(set(sound) - set(animal_sound))
    for j in sound:
        if j in fox:
            print(j, end=" ")
