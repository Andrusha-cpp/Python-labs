def unique_elements(list_):
    res_list = []
    for el in list_:
        if type(el) == list:
            list_in = unique_elements(el)
            for el_in in list_in:
                if el_in not in res_list:
                    res_list.append(el_in)
        elif el not in res_list:
            res_list.append(el)

    return res_list

listik = [8, 2, 4, [3, 4, 5, [3, 4, 6]], [1, 8]]
print(unique_elements(listik))