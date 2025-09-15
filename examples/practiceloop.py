# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1):   #i , n
#         print("*", end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i , n):
#         print(" ", end=' ')
#     for k in range(i + 1):
#         print("*", end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=' ')
#     for k in range(i, n):
#         print("*", end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i , n):
#         print(" ", end=' ')
#     for k in range(i):
#         print("*", end=' ')
#     for k in range(i + 1):
#         print("*", end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=' ')
#     for k in range(i , n - 1):
#         print("*", end=' ')
#     for k in range(i , n):
#         print("*", end=' ')
#     print()



# n = int(input("Enter the row size for the pattern: "))
# for i in range(n - 1):
#     for j in range(i , n):
#         print(" ", end=' ')
#     for k in range(i):
#         print("*", end=' ')
#     for k in range(i + 1):                                            
#         print("*", end=' ')
#     print()
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=' ')
#     for k in range(i , n - 1):
#         print("*", end=' ')
#     for k in range(i , n):
#         print("*", end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i,n):  #i + 1
#         print("1", end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1): 
#         print(i + 1, end=' ')
#     print()

# n = int(input("Enter the row size for the pattern: "))
# p = 0
# for i in range(n):
#     for j in range(i + 1): 
#         print(p, end=' ')
#     p += 2
#     print()

# n = int(input("Enter the row size for the pattern: "))
# p = n
# for i in range(n):
#     for j in range(i + 1): 
#         print(p, end=' ')
#     p -= 1
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1):
#         if (i % 2 == 0):
#             print("1", end=' ')
#         else:
#             print("2", end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# p = 1
# for i in range(n - 1):
#     for j in range(i , n):
#         print(' ', end=' ')
#     for k in range(i):
#         print(p, end=' ')
#     for k in range(i + 1):                                            
#         print(p, end=' ')
#     p += 1                                                                                      
#     print()
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=' ')
#     for k in range(i , n - 1):
#         print(p, end=' ')
#     for k in range(i , n):
#         print(p, end=' ')
#     p += 1   # p -= 1 is incrementing the value of p
#     print()

# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     p = 1
#     for j in range(i + 1):
#         print(' ', end=' ')
#     for k in range(i,n):
#         print(p , end=' ')
#         p += 1
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     p = 1
#     for j in range(i + 1):
#         print(p , end=' ')
#         p += 1
#     print()

# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):  
#     p = 1
#     for j in range(i , n):
#         print(' ', end=' ')
#     for k in range(i):
#         print(p , end=' ')
#         p += 1
#     for k in range(i + 1):
#         print(p , end=' ')
#         p += 1  
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     p = 5
#     for j in range(i + 1):
#         print(p , end=' ')
#         p -= 1
#     print()


# n = int(input("Enter the row size for the pattern: "))
# k = 5
# for i in range(n):
#     p = k
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(i, n):
#         print(p , end=' ')
#         p -= 1
#     k -= 1
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     p = 1
#     for j in range(i, n):
#         print(' ', end=' ')
#     for k in range(i):
#         print(p , end=' ')
#         p += 1
#     for k in range(i + 1):
#         print(p , end=' ')
#         p -= 1
#     print()


# n = int(input("Enter the row size for the pattern: "))
# p = 1
# for i in range(n):
#     for j in range(i + 1):
#         print(p , end=' ')
#         p += 1
#     print()


# rows = 6
# for i in range(0, rows):
#     for j in range(rows - 1, i, -1):
#         print(j, '', end='')
#     for l in range(i):
#         print('    ', end='')
#     for k in range(i + 1, rows):
#         print(k, '', end='')
#     print('\n')


# rows = 6
# for i in range(1, rows):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print("")



# n = int(input("Enter the row size for the pattern: "))
# for i in range(1,n + 1):
#     for j in range(1, i + 1):
#         # multiplication current column and row
#         s = i * j
#         print(i * j, end='  ')
#     print()

# rows = 16
# print("*" * rows, end="\n")
# i = (rows // 2) - 1
# j = 2
# while i != 0:
#     while j <= (rows - 2):
#         print("*" * i, end="")
#         print("_" * j, end="")
#         print("*" * i, end="\n")
#         i = i - 1
#         j = j + 2





# * character pattern
#65 to 90 A to Z //  a to z 97 to 122  // 0 to 9 48 to 57

# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1):
#         print('A', end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + i), end=' ')
#     print()

 
# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):  
#     for j in range(i + 1):
#         print(chr(69 - i), end=' ')
#     print()



# n = int(input("Enter the row size for the pattern: "))
# p = 65 
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(p), end=' ')
#     p += 2
#     print()


# for i in range(5):  
#     ch = chr(65 + i * 2) #i * 2 adds even-numbered offsets (0, 2, 4, 6, 8) on each iteration. index number *2
#     for j in range(i + 1):
#         print(ch, end=' ')
#     print()


# n = int(input("Enter the row size for the pattern: "))
# for i in range(n):
#     for j in range(i + 1):
#         if (i % 2 == 0):
#             print('A', end=' ')
#         else:
#             print('B', end=' ')
#     print() 


# n = 5
# for i in range(n):      
#     for j in range(i + 1):
#         if (i % 1 == 0):
#             print(chr(65 + i), end=' ')
#     print()