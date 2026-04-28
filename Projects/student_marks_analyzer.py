marks = []

for i in range(5):
    while True:
        try:
            num = int(input(f"Enter mark {i+1} (0-100): "))

            if num < 0 or num > 100:
                print(" Enter a valid mark between 0 and 100")
            else:
                marks.append(num)
                break

        except ValueError:
            print(" Please enter a number only")

print("\nMarks:", marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", sum(marks)/len(marks))
print("Sorted (ascending):", sorted(marks))
print("Sorted (descending):", sorted(marks, reverse=True))


grades = []

for mark in marks:
    if mark >= 90:
        grades.append("A")
    elif mark >= 75:
        grades.append("B")
    elif mark >= 50:
        grades.append("C")
    else:
        grades.append("F")

print("\nGrade Summary:")
print("A:", grades.count("A"))
print("B:", grades.count("B"))
print("C:", grades.count("C"))
print("F:", grades.count("F"))
