def string_comparassion(str1, str2):
    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False
    else:
        return False