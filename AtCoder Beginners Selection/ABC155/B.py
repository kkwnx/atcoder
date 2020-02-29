n = int(input())
a_list = list(map(int,input().split()))
f_denied = 0

for i in range(n):
    if a_list[i] % 2 == 0:
        # 偶数
        if a_list[i] % 3 != 0 and a_list[i] % 5 != 0:
            f_denied = f_denied + 1

if f_denied != 0:
    print("DENIED")
else:
    print("APPROVED")