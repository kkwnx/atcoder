def search_group(a):
    if a in zone_one:
        ret = 1
    elif a in zone_two:
        ret = 2
    else:
        ret = 3
    return ret

zone_one = {1,3,5,7,8,10,12}
zone_two = {4,6,9,11}
zone_three = {2}

x,y = map(int,input().split())

ret_x = search_group(x)
ret_y = search_group(y)

if ret_x == ret_y:
    print("Yes")
else:
    print("No")
