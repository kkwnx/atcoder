a,b,c = map(int,input().split())
same_count = 0
if a == b:
	same_count += 1
if a == c:
	same_count += 1
if b == c:
	same_count += 1
	
if same_count == 0:
	print(3)
elif same_count == 1:
	print(2)
else:
	print(1)
