# Program to find largest among 5 numbers

nums = []

for i in range(5):
    n = int(input("Enter number: "))
    nums.append(n)

print("Largest number is:", max(nums))
