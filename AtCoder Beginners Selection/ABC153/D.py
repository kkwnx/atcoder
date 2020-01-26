import math
h = int(input())

tmp = int(math.log2(h) + 1)
print(2 ** tmp - 1)
