h,a = map(int,input().split())
a_list = list(map(int,input().split()))

power_sum = 0
for i in range(len(a_list)):
    power_sum += a_list[i]

if power_sum >= h:
    print("Yes")
else:
    print("No")