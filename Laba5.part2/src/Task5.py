def merge_dicts(dict1, dict2):

    for key, value in dict2.items():
        if key in dict1:
            if type(value) == dict and type(dict1[key]) == dict:
                merge_dicts(dict1[key], value)
            else:
                dict1[key] = value
        else:
            dict1[key] = value