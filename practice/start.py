# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

#------------------------------------------------------------
# n = int(input("Enter a number: "))
# for i in range(n , 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

#------------------------------------------------------------
# n = int(input("Enter a number: "))
# for i in range(n , 0, -1):
#     for j in range(i , n):
#         print(" ", end=" ")
#     for k in range(1,i + 1):
#         print("*", end=" ")
#     print()

#------------------------------------------------------------
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     for j in range(i , n):
#         print(" ", end=" ")
#     for k in range(1,i + 1):
#         print("*", end=" ")
#     print()
#------------------------------------------------------------
# n = int(input("Enter a number: "))
# for i in range(1,n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end=" ")
#     print()

#------------------------------------------------------------
# n = int(input("Enter a number: "))
# for i in range(1,n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("1", end=" ")
#     print()

#------------------------------------------------------------

# n = int(input("Enter a number: "))
# for i in range(1,n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print(i, end=" ")
#     print()

#------------------------------------------------------------

# n = int(input("Enter a number: "))
# for i in range(1 , n + 1):
#     print(" " * (n - i) + "* " * i)
# for i in range(n , 0 , -1):
#     print(" " * (n - i + 1) + "* " * (i - 1))

#-------------------------------------------------------------

# n = int(input("Enter a number: "))
# for i in range(1 , n + 1):
#     print("" * (i + 1) + "*" * i)

# for i in range(n , 0 , -1):
#     print("" * (i + 1) + "*" * (i-1))


#------------------------------------------------------------

rows = int(input("Enter a numbers of rows: "))
cols = int(input("Enter a numbers of columns: "))
def mixed_value(rows,cols):
    alpha = 65
    number = 1
    for i in range(rows):
        for j in range(cols):
            if i % 2 == 0:
                print(chr(alpha), end=" ")
                alpha += 1
            else:
                print(number, end=" ")
                number += 1
        print()
mixed_value(rows, cols)