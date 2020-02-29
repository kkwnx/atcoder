a,b,c = map(int,input().split())
anser_list = []
anser_list.append(abs(b-a) + abs(c-b))
anser_list.append(abs(c-a) + abs(b-c))
anser_list.append(abs(a-b) + abs(c-a))
anser_list.append(abs(c-b) + abs(a-c))
anser_list.append(abs(a-c) + abs(b-a))
anser_list.append(abs(b-c) + abs(a-b))

print(min(anser_list))
