candy_bag = list(map(int, input().split()))
max_bag_num = max(candy_bag)
bag = 0
small_bag_sum = 0
for bag in candy_bag:
	if bag == max_bag_num:
		continue
	else:
		small_bag_sum += bag

if max_bag_num == small_bag_sum:
	print("Yes")
else:
	print("No")
