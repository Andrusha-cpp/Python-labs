user_number = int(input("Input your number:"))
if user_number % 7 == 0:
    print("Magic number!")
else:
    print(sum(map(int, str(user_number))))