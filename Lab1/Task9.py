IP = input("Enter IP-adress: ")

try: #check1
    num1, num2, num3, num4 = map(int, IP.split("."))
except ValueError:
    print("Incorrect IP-adress")

try:
    if all(0 <= n <= 255 for n in (num1, num2, num3, num4)): #check2
        print("Correct IP-adress.")
    else:
        print("Incorrect IP-adress")
except NameError:
    print("Incorrect IP-adress")