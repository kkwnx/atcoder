renga_num = int(input())
renga_line = list(map(int,input().split()))

num = 1
break_num = 0
for i in range(0,renga_num):
    if renga_line[i] != num:
        break_num += 1
    else:
        num += 1

if break_num == renga_num:
    print(-1)
else:
    print(break_num)