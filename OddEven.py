input_line = input()
a,b = input_line.split()
c = int(a) * int(b)
if c % 2 == 0:
    print("Even")
else:
    print("Odd")