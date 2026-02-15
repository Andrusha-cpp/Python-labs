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