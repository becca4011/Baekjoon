"""
L = int(input())
hash = input()

li = list(hash)
sum = 0
n = 0

for i in li:
    sum += (ord(i) - 96) * 31 ** n
    n += 1

print(sum)
"""

hash = {}

for i in range(26):
    hash[chr(i + 97)] = i + 1

L = int(input())
H = input()

li = list(H)
sum = 0

for i in range(L):
    sum += hash[li[i]] * 31 ** i

print(sum % 1234567891)