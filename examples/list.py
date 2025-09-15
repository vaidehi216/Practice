# a = [10, 15, 20, 25]

# # Doubling even numbers
# a = [x * 2 if x % 2 == 0 else x for x in a]
# print(a)

# 'both condition checks '


# fruits = ['apple', 'banana', 'cherry']
# fruits.remove("banana")
# print(fruits)



# fruits = ['apple', 'banana', 'cherry']
# fruits.pop("1")
# print(fruits)

# pop are usinhg index
# remove is using value 


# numbers = [1, 2, 3, 4, 5, 7, 6, 7, 8, 9, 10, 1, 5]
# unique_numbers = list(set(numbers))
# duplicates = len(numbers) - len(unique_numbers)
# print(f"Number of duplicate elements: {duplicates}")
# print(f"Unique elements: {unique_numbers}")


numbers = [1, 2, 5, 7, 6, 7, 10, 1, 5, 1, 9] 
duplicates = []
for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
         duplicates.append(i)
print(f"Numbers in the list: {len(numbers)}\n")
print(f"Unique number : {len(list(set(numbers)))}")
print(f"Unique elements: {list(set(numbers))}\n")
print(f"Duplicate elements: {len(duplicates)}")
print(f"Duplicate elements: {duplicates}\n") 