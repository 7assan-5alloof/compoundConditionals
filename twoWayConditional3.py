clockHour = int(input("Enter current clock (only hour, 24-h format): "))
if (0 <= clockHour) and (clockHour < 12):
    print("The time you entered is before noon (AM)")
if (clockHour >= 12) and (clockHour <= 23):
    print("The time you entered is noon or after (PM)")
else:
    print("Invalid clock, please run the program and try again")
