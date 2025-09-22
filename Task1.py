name = input("Enter your name: ")
surname = input("Enter your surname: ")
otchestvo = input("Enter name by father: ")

full_name = surname + ' ' + name[0].upper() + '.' + otchestvo[0].upper() + '.'
print(full_name)