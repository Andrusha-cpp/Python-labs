pressure = float(input("Enter pressure in Pa: "))
volume = float(input("Enter volume in m^3: "))
temperature = float(input("Enter temperature in K: "))

R = 8.32
print(f"P = {pressure} Pa\nV = {volume} m^3\nT = {temperature} K\nR = {R}")

n = round((pressure * volume) / (R * temperature), 4)
print(f"Answer: n = {n} moles") 