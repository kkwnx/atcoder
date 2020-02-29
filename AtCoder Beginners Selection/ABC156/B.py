n,k = map(int,input().split())
i = 1
while 1:
    if n < k:
        print(1)
        break
    if n < k ** i and n > k ** (i - 1):
        print(i)
        break
    if n == k ** i:
        print(i + 1)
        break
    else:
        i = i + 1

