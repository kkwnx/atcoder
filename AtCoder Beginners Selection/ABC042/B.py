input_map = []
string_num, string_length = map(int, input().split())
for i in range(string_num):
    input_line = input()
    input_map.append(input_line)

input_map.sort()

line = ""
for i in range(string_num):
    line = line + input_map[i]

print(line)