marks = []

for i in range(5):
    num = int(input(f"Enter mark {i+1}:  "))
    marks.append(num)

print("\nMarks:", marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", sum(marks)/len(marks))
print("Sorted (ascending):", sorted(marks))
print("Sorted (descending):", sorted(marks, reverse=True))

for mark in marks:
    if mark >= 90:
        print(f"Mark {mark} is an A grade")
    elif mark >= 75:
        print(f"Mark {mark} is a B grade")
    elif mark >= 50:
        print(f"Mark {mark} is a C grade")
    else:
        print(f"Mark {mark} is a F grade")
