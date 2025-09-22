import math

summa = int(input("Enter summa: "))
denomination = {100: 0, 50: 0, 10: 0, 5: 0, 2: 0, 1: 0}
print(denomination)

for key in denomination:
    amount = math.floor(summa / key) #amount of current nominee
    if amount >= 1:
        denomination[key] += amount
        summa = summa % key
    else:
        continue

for key, value in denomination.items():
    print(key, "- ", value)