def polindrom_check(string):
    rev_string = string[::-1]

    if string == rev_string:
        return True
    else:
        return False
    
    