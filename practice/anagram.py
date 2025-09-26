str1 = input("Enter first name: ")
str2 = input("Enter second name: ")

if sorted(str1) == sorted(str2):
    print("The names are anagrams.")
else:
    print("The names are not anagrams.")

