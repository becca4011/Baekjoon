"""
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n - 1) + fibo(n - 2))

for i in range(1, 10):
    print(fibo(i))
"""

fibo = [0]
for x in range(1, 10):
    if x < 2:
        fibo.append(1)
    else:
        fibo.append(fibo[x - 2] + fibo[x - 1])

print(fibo)
