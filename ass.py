# в строке пользователя если больше 10 и больше 100 сущ и цифры и буквы заменить цифры на пробелы иначе вывести строку в обратном порядке

string = input("Enter the string: ")
str_length = len(string)

num_check = False

if '0' in string:
    num_check = True
if '1' in string:
    num_check = True
if '2' in string:
    num_check = True
if '3' in string:
    num_check = True
if '4' in string:
    num_check = True
if '5' in string:
    num_check = True
if '6' in string:
    num_check = True
if '7' in string:
    num_check = True
if '8' in string:
    num_check = True
if '9' in string:
    num_check = True

alpha_check = False

if 'a' in string:
    alpha_check = True
if 'b' in string:
    alpha_check = True
if 'c' in string:
    alpha_check = True
if 'd' in string:
    alpha_check = True
if 'e' in string:
    alpha_check = True
if 'f' in string:
    alpha_check = True
if 'g' in string:
    alpha_check = True
if 'h' in string:
    alpha_check = True
if 'j' in string:
    alpha_check = True
if 'k' in string:
    alpha_check = True
if 'l' in string:
    alpha_check = True
if 'm' in string:
    alpha_check = True
if 'n' in string:
    alpha_check = True
if 'o' in string:
    alpha_check = True
if 'p' in string:
    alpha_check = True
if 'q' in string:
    alpha_check = True
if 'r' in string:
    alpha_check = True
if 's' in string:
    alpha_check = True
if 't' in string:
    alpha_check = True
if 'u' in string:
    alpha_check = True
if 'v' in string:
    alpha_check = True
if 'w' in string:
    alpha_check = True
if 'x' in string:
    alpha_check = True
if 'y' in string:
    alpha_check = True
if 'z' in string:
    alpha_check = True


if str_length < 11:
    print(string[::-1])
elif str_length > 100:
    print(string[::-1])
else:
    if num_check and alpha_check:
        string = string.replace('0', " ")
        string = string.replace('1', " ")
        string = string.replace('2', " ")
        string = string.replace('3', " ")
        string = string.replace('4', " ")
        string = string.replace('5', " ")
        string = string.replace('6', " ")
        string = string.replace('7', " ")
        string = string.replace('8', " ")
        string = string.replace('9', " ")

print(string)
        

