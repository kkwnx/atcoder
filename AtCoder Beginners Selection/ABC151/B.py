n,k,m = map(int,input().split())
point_list = list(map(int,input().split()))

point_total = 0
for i in point_list:
    point_total = point_total + i

x = m * n - point_total
if x < 0:
    print(0)
elif x > k:
    print(-1)
else:
    print(x)