# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print("*", end=" ")   # Print star
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print("#", end=" ")
#     print()
          # Outer loop for rows




# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows, 0, -1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1,rows + 1):  # Upper part of diamond
#     for j in range(rows  - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()
# for i in range(rows  - 1, 0, -1):  # Lower part of diamond
#     for j in range(rows  - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, rows + 1):  # Inner loop for columns
#         if i == 1 or i == rows or j == 1 or j == rows :  # Print star only on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         if j == 1 or i == rows or i == j:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()



# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows,0, - 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         if j == 1 or i == rows or i == j:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()



# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows,0, - 1):  
#     for j in range(rows  - i):  
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         if k == 1 or k == 2 * i - 1 or i == rows:  
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Upper part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         if k == 1 or k == 2 * i - 1:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()
# for i in range(rows - 1, 0, -1):  # Lower part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         if k == 1 or k == 2 * i - 1:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()


# rows = int(input("Enter the row size for the pattern:"))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print(j, end=" ")  # Print numbers
#     print()


# rows = int(input("Enter the row size for the pattern:"))
# for i in range(rows,0,-1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print(j, end=" ")  # Print numbers
#     print()



# rows = int(input("Enter the row size for the pattern:"))
# for i in range(1, rows + 1):  
#     for j in range(1, i + 1):  
#         print(j, end=" ")  
#     print()
# for i in range(rows,0,-1):  
#     for j in range(1, i + 1):  
#         print("@", end=" ")  
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, i + 1):  # Inner loop for numbers
#         print(k, end=" ")
#     for l in range(i - 1, 0, -1):  # Inner loop for reverse numbers
#         print(l, end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows,0,-1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, i + 1):  # Inner loop for numbers
#         print(k, end=" ")
#     for l in range(i - 1, 0, -1):  # Inner loop for reverse numbers
#         print(l, end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Upper part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(k, end=" ")
#     for l in range(i - 1, 0, -1):
#         print(l, end=" ")
#     print()
# for i in range(rows - 1, 0, -1):  # Lower part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(k, end=" ")
#     for l in range(i - 1, 0, -1):
#         print(l, end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print(chr(64 + j), end=" ")  # Print alphabets
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows, 0, -1):  
#     for j in range(1, i + 1):  
#         print(chr(64 + j), end=" ")  
#     print()



# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, i + 1):  # Inner loop for alphabets
#         print(chr(64 + k), end=" ")
#     for l in range(i - 1, 0, -1):  # Inner loop for reverse alphabets
#         print(chr(64 + l), end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows, 0, -1):
#     for j in range(rows - i): 
#         print(" ", end=" ")
#     for k in range(1, i + 1):  
#         print(chr(64 + k), end=" ")
#     for l in range(i - 1, 0, -1):  
#         print(chr(64 + l), end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Upper part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(chr(64 + k), end=" ") #64 is an ASCII value for 'A'
#     for l in range(i - 1, 0, -1):
#         print(chr(64 + l), end=" ")
#     print()
# for i in range(rows - 1, 0, -1):  # Lower part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(chr(64 + k), end=" ")
#     for l in range(i - 1, 0, -1):
#         print(chr(64 + l), end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print(chr(64 + j), end=" ")  # Print alphabets
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows,0,-1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print(chr(64 + j), end=" ")  # Print alphabets
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, i + 1):  # Inner loop for alphabets
#         print(chr(64 + k), end=" ")
#     for l in range(i - 1, 0, -1):  # Inner loop for reverse alphabets
#         print(chr(64 + l), end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows,0,-1):  # Outer loop for rows
#     for j in range(rows - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, i + 1):  # Inner loop for alphabets
#         print(chr(64 + k), end=" ")
#     for l in range(i - 1, 0, -1):  # Inner loop for reverse alphabets
#         print(chr(64 + l), end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Upper part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(chr(64 + k), end=" ")
#     for l in range(i - 1, 0, -1):
#         print(chr(64 + l), end=" ")
#     print()
# for i in range(rows - 1, 0, -1):  # Lower part of diamond
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(chr(64 + k), end=" ")
#     for l in range(i - 1, 0, -1):
#         print(chr(64 + l), end=" ")
#     print()



# rows = int(input("Enter the row size for the pattern: "))
# num = 1   # change the 2 so that it can print even numbers
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print(num, end=" ")  # Print numbers in sequence
#         num += 2
#     print()



# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows ):  # Outer loop for rows
#     num = 1
#     for j in range(rows - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(i + 1):  # Inner loop for numbers
#         print(num, end="   ")
#         num = num * (i - k) // (k + 1)  # Calculate Pascal's number
#     print()




# rows = int(input("Enter number of rows: "))

# # Upper half
# for i in range(1, rows + 1):
#     print("*" * i + " " * (2 * (rows - i)) + "*" * i)

# # Lower half
# for i in range(rows, 0, -1):
#     print("*" * i + " " * (2 * (rows - i)) + "*" * i)




# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Upper part of butterfly
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(2 * (rows - i)):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(rows, 0, -1):  # Lower part of butterfly
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(2 * (rows - i)):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, rows + 1):  # Inner loop for columns
#         print(j, end=" ")  # Print numbers
#     print()



# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, rows + 1):  # Inner loop for columns
#         if i == 1 or i == rows or j == 1 or j == rows:  # Print numbers only on borders
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()  # Move to the next line



# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, rows + 1):  # Inner loop for columns
#         if (i + j) % 2 == 0:  # Print numbers in zig-zag pattern
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()


# rows = int(input("Enter the row size for the pattern:"))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, rows + 1):  # Inner loop for columns
#         if i == j or i + j == rows + 1:  # Print stars in cross pattern
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space
#     print()


# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, rows  + 1):  # Inner loop for columns
#         if i == rows  // 2 + 1 or j == rows  // 2 + 1:  # Print stars in plus pattern
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space
#     print()


# rows = 5
# for i in range(1, rows + 1): 
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(0, rows - i + 1):
#             print("*", end=" ")
#     print()


n = 5 
for i in range(n + 1):
    for j in range(n - i):   # i + 1 , n + 1
        print("  ", end="")
    for k in range(i):
        print("*", end="   ") 
    print() 

