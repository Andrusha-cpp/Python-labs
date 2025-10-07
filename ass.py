#если в строке больше 15 и только буквы то каждый пятый, если не только и длинна кратна 5 то вывести "отчислен"

string = input("Input string:")

alpha_check = string.isalpha()

num_check = string.isdigit()


if alpha_check:
    if len(string) > 15:
        print(string[::5])
    elif len(string) % 5 == 0:
        print("Отчислен")


