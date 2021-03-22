N = int(input())

if len(str(N)) == 1 and N % 2 != 0:
    print(0)
else:
    for i in range(1, N):
        # 방법 1
        nsum = map(int, list(str(i)))
        lsum = i + sum(nsum)

        """
        # 방법 2
        L = len(str(i))
        lsum = i
        for j in range(1, L+1):
            lsum += i // 10 ** (L - j) % 10
        """

        if lsum == N:
            print(i)
            break

        elif i == N - 1:
            print(0)