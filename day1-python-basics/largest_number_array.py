#ask for the size
size_of_list=int(input("Enter the size of an array: "))

list=[]

for i in range(size_of_list):
    num=int(input("Enter the number into the list: "))
    
    #append it into the list
    
    list.append(num)
# assume the largest is the element at the first index
largest_number = list[0]

for i in range(size_of_list):
    #compare the elements in the list againt the element at the first index
    if list[i] > largest_number:
        #if the condition is met,update the largest element by assigning that bigger element to it
        
        largest_number=list[i]

print(list)
print(f"The largest element is {largest_number}")
    