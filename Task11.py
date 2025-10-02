print("Enter date of birthday:")
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

print(day, month, year) 

print("Zodiac sign is", end=" ") #selection of zodiac sign 
if month == 1:
    if day < 20:
        print("Goat")
    else:
        print("Water Bearer")
elif month == 2:
    if day < 19:
        print("Water Bearer")
    else:
        print("Fish")
elif month == 3:
    if day < 21:
        print("Fish")
    else:
        print("Ram")
elif month == 4:
    if day < 20:
        print("Ram")
    else:
        print("Bull")
elif month == 5:
    if day < 21:
        print("Bull")
    else:
        print("Twins")
elif month == 6:
    if day < 22:
        print("Twins")
    else:
        print("Crab")
elif month == 7:
    if day < 23:
        print("Crab")
    else:
        print("Lion")
elif month == 8:
    if day < 23:
        print("Lion")
    else:
        print("Virgin")
elif month == 9:
    if day < 23:
        print("Virgin")
    else:
        print("Balance")
elif month == 10:
    if day < 24:
        print("Balance")
    else:
        print("Scorpion")
elif month == 11:
    if day < 22:
        print("Scorpion")
    else:
        print("Archer")
elif month == 12:
    if day < 22:
        print("Archer")
    else:
        print("Goat")


