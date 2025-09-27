summa = int(input("Enter summa: "))
denomination = {100: 0, 50: 0, 10: 0, 5: 0, 2: 0, 1: 0}
print(denomination)

if summa >= 100:
    amount = summa // 100
    denomination[100] += amount
    summa = summa % 100

if summa >= 50:
    amount = summa // 50
    denomination[50] += amount
    summa = summa % 50

if summa >= 10:
    amount = summa // 10
    denomination[10] += amount
    summa = summa % 10

if summa >= 5:
    amount = summa // 5
    denomination[5] += amount
    summa = summa % 5

if summa >= 2:
    amount = summa // 2
    denomination[2] += amount
    summa = summa % 2

if summa >= 1:
    amount = summa // 1
    denomination[1] += amount
    summa = summa % 1

print(f"100 - {denomination[100]}",
      f"50 - {denomination[50]}",
      f"10 - {denomination[10]}",
      f"5 - {denomination[5]}",
      f"2 - {denomination[2]}",
      f"1 - {denomination[1]}", sep="\n")