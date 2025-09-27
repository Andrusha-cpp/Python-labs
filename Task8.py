string = input("Enter string: ")
reversed_str = "".join(reversed(string))

if string == reversed_str:
    print("It's polindrom")
else:
    print("It's not polindrom")