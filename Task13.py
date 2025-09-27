import random

guess_num = random.randint(1, 100)

while True:
    user_num = int(input("Input number:"))
    if user_num == guess_num:
        print("Congrats!!! You win!!!")
        break
    elif user_num > guess_num:
        print("Too big(((")
    elif user_num < guess_num:
        print("Too small(((")
