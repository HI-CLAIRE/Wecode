my_list = ["one", 2, 3, 2, "one"]

def make_dic(lst):
    cnt_lst = []
    ans = []
    x = 0
    for i in lst:

        cnt_lst.append(lst.count(i))
        ans.append([lst[x], cnt_lst[x]])
        x += 1
    return(dict(ans))
print(make_dic(my_list))