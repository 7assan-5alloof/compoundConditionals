mark = int(input("Enter your mark: "))
print("Grade", end=" ")

if mark < 0 or mark > 100:
    print("Invalid mark, please run the program and give a real mark.")
elif mark >= 90:
    print("A*")
elif mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
else:
    print("D")
