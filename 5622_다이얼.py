# ABC  : 2
# DEF  : 3
# GHI  : 4
# JKL  : 5
# MNO  : 6
# PQRS : 7
# TUV  : 8
# WXYZ : 9

al = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
st = input()

n = -1
sum = 0
while (n != len(st) - 1):
    n += 1
    for i in range(8):
        for a in al[i]:
            if st[n] == a:
                sum += i + 3

print(sum)

