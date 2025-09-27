date_str = input("Enter date of birthday (example: 31.01.2024):")

try:
    day, month, year = map(int, date_str.split(".")) #check that data has only numbers and points
    print(day, month, year) 
except ValueError:
    print("Incorrect data. Restart programm and try again.")
    exit() 

if (day or month or year) <= 0 or day > 31 or month > 12: #check that data have correct numbers 
     print("Incorrect data. Restart programm and try again.")
     exit()

print("Zodiac sign is", end=" ") #selection of zodiac sign 
match month:
    case 1:
        if day < 20:
            print("Goat")
        else:
            print("Water Bearer")
    case 2:
        if day < 19:
            print("Water Bearer")
        else:
            print("Fish")
    case 3:
        if day < 21:
            print("Fish")
        else:
            print("Ram")
    case 4:
        if day < 20:
            print("Ram")
        else:
            print("Bull")
    case 5:
        if day < 21:
            print("Bull")
        else:
            print("Twins")
    case 6:
        if day < 22:
            print("Twins")
        else:
            print("Crab")
    case 7:
        if day < 23:
            print("Crab")
        else:
            print("Lion")
    case 8:
        if day < 23:
            print("Lion")
        else:
            print("Virgin")
    case 9:
        if day < 23:
            print("Virgin")
        else:
            print("Balance")
    case 10:
        if day < 24:
            print("Balance")
        else:
            print("Scorpion")
    case 11:
        if day < 22:
            print("Scorpion")
        else:
            print("Archer")
    case 12:
        if day < 22:
            print("Archer")
        else:
            print("Goat")


