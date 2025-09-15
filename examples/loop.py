# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# index = 0
# while index < len(nums):
#     print(nums[index])
#     index +=1






nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

input_num = int(input("enter a number: "))
i = 0
while i < len(nums):
    if nums[i] == input_num:
        print("found it at index: ", i)
        break   #using the stop loop
    else:
         print("finding...")
    i += 1  