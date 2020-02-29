n = int(input())
max_num = 0
s_dic = {}
for i in range(n):
    input_line = input()
    if input_line in s_dic:
        s_dic[input_line] = s_dic[input_line] + 1
    else:
        s_dic[input_line] = 1
    if s_dic[input_line] > max_num:
        max_num = s_dic[input_line]

anser_list = []
for key,value in s_dic.items():
    if value == max_num:
        anser_list.append(key)

anser_list.sort()
for key in anser_list:
    print(key)
