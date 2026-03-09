nums=[4,1,8,3,8,2]
count=0
for i in range(len(nums)):
    if nums[i] == 8:
        count += 1
print(count)