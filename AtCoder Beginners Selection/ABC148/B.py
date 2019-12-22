n = int(input())
s, t = input().split()

line = ""

for i in range(n):
    line += s[i]
    line += t[i]

print(line)
