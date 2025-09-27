pressure = float(input("Enter pressure in Pa: "))
volume = float(input("Enter volume in m^3: "))
temperature = float(input("Enter temperature in K: "))
R = 8.32

n = round((pressure * volume) / (R * temperature), 4)
print("Answer: n =", n, "moles") 