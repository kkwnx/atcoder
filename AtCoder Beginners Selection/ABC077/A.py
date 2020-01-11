line1 = input()
line2 = input()

if line1[0] == line2[2] and line2[0] == line1[2] and line1[1] == line2[1]:
    print("YES")
else:
    print("NO")