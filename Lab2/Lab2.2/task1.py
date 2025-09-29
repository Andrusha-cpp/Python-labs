def flat_list(list_):
    i = 0
    while i < len(list_):
        if type(list_[i]) == list:
            list_[i] = flat_list(list_[i])
            list_[i:i+1] = list_[i] 
        else:
            i += 1

    return list_

list_ = [1, 2, [3, 4, 5, [6, 7]], 8, [9]]
new_list = flat_list(list_)
print(new_list)