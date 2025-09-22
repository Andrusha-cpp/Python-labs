password = input("Enter your password: ")

if len(password) < 16:
    print("Too short(((")
    if password.isdigit():
        print("Too weak(((")
    elif password.isalpha():
        print("Too weak(((")
else:
    if password.isdigit():
        print("Too weak(((")
    elif password.isalpha():
        print("Too weak(((")
    else:
        print("Strong password")
