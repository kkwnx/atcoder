n,m = map(int,input().split())
ac_list = [0] * (n + 1)
wa_list = [0] * (n + 1)

for i in range(m):
    q_no_tmp,anser = input().split()
    q_no = int(q_no_tmp)
    if anser == "AC":
        ac_list[q_no] = 1
    else:
        if ac_list[q_no] != 1:
            wa_list[q_no] = wa_list[q_no] + 1 

wa_num = 0
ac_num = 0
for i in range(n + 1):
    if ac_list[i] != 1:
        wa_list[i] = 0
    else:
        ac_num = ac_num + 1
    wa_num = wa_num + wa_list[i]

print(ac_num,wa_num)
