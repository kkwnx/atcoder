attack_num = 1
def attack(x):
    global attack_num
    if x == 1:
        return 1
    x = x // 2
    return 2*attack(x) + 1

h = int(input())
print(attack(h))