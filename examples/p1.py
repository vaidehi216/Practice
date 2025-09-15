# for i in range(3):
#    print(i, end =' ')
 

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("result: ", result)
# except ValueError:
#     print("That's not a valid number.", result)
# except ZeroDivisionError:
#     print("Can't divide by zero.", result)



# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found.")


# class MyNumber:
#     def __init__(self, value):
#         self.value = value

#     def __rshift__(self, other):
#         return self.value >> other

# obj = MyNumber(24)
# print(obj >> 2)  # Output: 8

# for i in range(5):
#    print(i, end=' ')

# total = 0
# for num in range(1, 6):
#    total += num
# print(total)
 
# for char in 'hello':
#    if char == 'l':
#        break
#    print(char, end=' ')

# numbers = [3, 7, 2, 3, 5]
# for i, num in enumerate(numbers):
#    if i == num:
#        break
#    print(num, end=' ') #index and loop value same so break the loop



# count = 0
# while count < 5:
#    print("Hello")
#    count += 1
# else:
#    print("Else block")





# num = 10
# while num > 0:
#    if num % 2 == 0:
#        print(num, end=" ")
#    num -= 1



# x = 1
# while x < 6:
#    print(x, end=" ")
#    x += 1
#    if x == 4:
#     continue

# x = 1
# while x < 6:
#     if x == 4:
#         x += 1
#         continue
#     print(x, end=" ")
#     x += 1



# count = 0
# while count < 5:
#    print("Count:", count)
#    count += 1
#    if count == 3:
#        continue
#    print("After Continue")


# square of 2 and 4 (8 & 16) so ans is Prints powers of 2 from 2 to 8
# num = 2
# while num < 10:
#    print(num, end=" ")
#    num **= 2


#Pass statement examples
# x = [1,2,3,4,5,10]
# for i in x:
#     if(i%5 == 0):
#         pass
#     else:
#         print(i)







# def hello():
#     pass
# print("Function defined")

# for i in range(4):
#     if i % 2 == 0:
#         print(i)
#     else:
#         pass



# n = int(input("Enter a number: "))
# for i in range(n):
#     if i % 2 == 0:
#         print(f"{i} is even")


# for i in range(1, 11):
#     if i % 2 == 0:
#         pass  # skip even numbers
#     else:
#         print(f"Odd number found: {i}")



# x = 23    #This is the Global Variable

# def fnc_name():   
#   x = 24     #This is Local Variable  
#   print(x)

# fnc_name()  
# print(x)  


# n = int(input("Enter a number: ")) 
# sum_cubes = sum(int(digit) ** 3 for digit in str(n)) 
# if n == sum_cubes:
#     print(f"The number {n} is an Armstrong number") 
# else:
#     print(f"The number {n} is not an Armstrong number") #153 , 123


