print("Enter consumed: ")
internet = int(input("Internet traffic (Mb): "))
minutes = int(input("talking minutes: "))
sms = int(input("sms messages: "))
payment = 24.99
tax = 1.002

print("Base Tariff:", payment)

if internet > 1000:
    add_internet = internet - 1000
    payment += add_internet * 0.79
    print(f"You have extra {add_internet} megabytes: + {round(add_internet, 2) * 0.79} rubles")
if minutes > 60:
    add_minutes = minutes - 60
    payment += add_minutes * 0.89
    print(f"You have extra {add_minutes} minutes: + {round(add_minutes, 2) * 0.89} rubles")
if sms > 30:
    add_sms = sms - 30
    payment += add_sms * 0.59
    print(f"You have extra {add_sms} messages: + {round(add_sms * 0.59, 2)} rubles")

print("Tax: 2%")
payment = round(payment * tax, 2)
print(f"Total payment: {payment}")