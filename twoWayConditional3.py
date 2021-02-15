clockHour = int(input("Enter current clock (only hour, 24-h format): "))
if (clockHour >= 0) and (clockHour <= 23):
    pass
else:
    quit(print("Invalid clock, please run program again"))
if clockHour < 12:
    print("The time you entered is before noon (AM)")
else:
    print("The time you entered is noon or after (PM)")
