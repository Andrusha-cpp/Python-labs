#в строке длина Ю 10 все глассные зам на цифру если только буквы то выведем каждый второй с конца если только цифры то найдем частное от деления на сто 

string = input("Enter string:")

if string.isdigit():
    string_digit = int(string)
    print(f"Result of division on 100: {string_digit / 100}")

if string.isalpha():
    print(f"If only letters: {string[::-2]}")

k = 1
if len(string) > 10:
    for letter in string:
        if letter in "aeiouAEIOU":
            string = string.replace(letter, str(k))
            k += 1
    print(f"Result: {string}")