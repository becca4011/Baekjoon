num = input().split()
sum = 0

for i in num:
    sq = int(i) * int(i)
    sum += sq

print(sum % 10)