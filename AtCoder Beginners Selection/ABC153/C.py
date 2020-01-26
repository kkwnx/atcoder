n,k = map(int,input().split())
h_list = list(map(int,input().split()))

h_list.sort(reverse=True)
attack_num = 0
for i in range(len(h_list) - k):
    attack_num += h_list[k + i]

print(attack_num)

