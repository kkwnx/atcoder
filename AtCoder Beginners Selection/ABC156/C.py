n = int(input())
xlist = list(map(int,input().split()))

xlist.sort()
#max_x = xlist[n - 1]
#min_x = xlist[0]

#p = int((max_x - min_x)/2) + min_x

s = sum(xlist)
p = round(s / n)
add_x = 0
for i in range(n):
    add_x = add_x + (xlist[i] - p) ** 2

print(add_x)