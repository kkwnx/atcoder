a, b = map(int,input().split())
min_num = min(a,b)
max_num = max(a,b)
for i in range(1,10**5 + 1):
    if min_num * i % max_num == 0:
        print(min_num * i)
        break

