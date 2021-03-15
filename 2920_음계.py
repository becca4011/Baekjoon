sg = input().split()
asc = 0
des = 0

for i in range(8):
    if int(sg[i]) == i + 1:
        asc += 1
    elif int(sg[i]) == 8 - i:
        des += 1

if asc == 8:
    print("ascending")
elif des == 8:
    print("descending")
else:
    print("mixed")