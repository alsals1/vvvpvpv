def find_pa(lst, word):
    if word == 1:
        return len(lst)
    else:
        cnt = 0
        re_lst = []
        for i in range(len(lst) - word + 1):
            if lst[i:i + word] == lst[i + word - 1:i - 1:-1]:
                cnt += 1
                re_lst.append(lst[i:i + word])
        print(re_lst)

list1 = [1,2,1,4,9,2,4,2,8,7,1,10,1]
find_pa(list1, 3)

