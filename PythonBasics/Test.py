marks = float(input("Enter Marks : "))
section = input("Enter the section - ")
if marks == 100:
    if section == "A":
        print("Brilliant class")
    grade = "A+"
    print(grade)
elif 80 < marks < 100:
    print("B")
elif 60 < marks < 80:
    print("C")
else:
    print("Student is failed")