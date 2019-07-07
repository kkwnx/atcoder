def devision2(numbers,num):
    return_numbers = []
    for n in range(num):
        return_numbers.append(int(numbers[n]) / 2)
    return return_numbers

num = int(input())
input_numbers = input().split()

end_num = 0
f_odd = 1
while f_odd:
    for n in range(num):
        if int(input_numbers[n]) == 0:
            f_odd = 0
            break
        if int(input_numbers[n]) % 2 != 0:
            f_odd = 0
            break
    if f_odd == 1:
        end_num += 1
        input_numbers = devision2(input_numbers,num)[:]

print(end_num)