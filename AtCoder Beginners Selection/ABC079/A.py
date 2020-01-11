n = input()
f_good = 0
if n[1] == n[2]:
    if n[0] == n[1] or n[2] == n[3]:
        f_good = 1

if f_good == 1:
    print("Yes")
else:
    print("No")