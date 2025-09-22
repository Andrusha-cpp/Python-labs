time = int(input("Seconds:"))

minutes = round(time / 60)
seconds = time % 60
print(minutes, "minutes", seconds, "seconds")