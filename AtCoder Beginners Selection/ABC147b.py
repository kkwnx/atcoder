line = input()
count = 0
for i in range(len(line)):
    if line[i] != line[len(line)-1-i]:
        count += 1
    if i + 1 >= len(line)/2:
        break

print(count)