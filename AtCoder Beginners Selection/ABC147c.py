# インプット情報を格納
member_num = int(input())
ans_table = []
for i in range(member_num):
    ans_num = int(input())
    ans = {}
    for k in range(ans_num):
        a,b = input().split()
        # 人を表すIDはインデックスを0オリジンにするために-1する
        ans[int(a) - 1] = b
    ans_table.insert(i,ans)

# 取りうる全パターン(誰が正直/不親切)を作成
# member_numの配列ｘ2^member_num
bin_str = []
for i in range(2**member_num):
    bin_line = format(i,'b').zfill(member_num)
    bin_str.append(bin_line)

#矛盾検索
contradiction = 0
anser_index = []
for i in range(2**member_num):
    for k in range(member_num):
        if bin_str[i][k] == "1":
            # ans_tableのk番目の回答は信用できると仮定
            for idnum, answer in ans_table[k].items():
                if bin_str[i][idnum] != answer:
                    # 矛盾あり
                    contradiction = 1
                    break
        if contradiction == 1:
            break
    # 矛盾がなかった
    if contradiction == 0:
        anser_index.append(i)
    contradiction = 0

honest = 0
for index in anser_index:
    honest_tmp = bin_str[index].count("1")
    if honest < honest_tmp:
        honest = honest_tmp
print(honest)

