string = input("Enter the string:")

dict_ = {}
for letter in string:
    if letter in dict_:
        dict_[letter] += 1
    else:
        dict_[letter] = 1

res_string = ""
for key, el in dict_.items():
    res_string = res_string + key + str(el)

print(res_string)