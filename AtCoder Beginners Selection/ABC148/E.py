import math


#sys.setrecursionlimit(5000)
#resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

#def func(a):
#    if a < 2:
#        return 1
#    return a * func(a - 2)

n = int(input())
#return_num = func(n)
return_num = math.factorial(n)
count = 0
while 1:
    if return_num % 10 == 0:
        count += 1
        return_num = return_num // 10
    else:
        break
print(count)

