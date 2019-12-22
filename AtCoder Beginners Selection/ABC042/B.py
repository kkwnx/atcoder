import itertools
input_map = []
string_num, string_length = map(int, input().split())
for i in range(string_num):
    input_line = input()
    input_map[i] = input_line
print_line = []
for k in range(string_num):
    for i in range(string_num - 1):
        if input_map[i] > input_map[i+1]:
            tmp_input_map = input_map[i]
            input_map[i+1] = input_map[i]
            input_map[i] = tmp_input_map

for k in rante(string_num):
    print_line.append(input_map[k])
print(print_line)

