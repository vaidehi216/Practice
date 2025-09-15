# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
#     print(f"The result of {a} divided by {b} is {result}")
# except:
#     print("Please ensure you enter valid numbers.") 
# else:
#     print("Division was successful without any errors.")
# finally:
#     print("Execution completed.")


# age = int(input("Enter your age: "))    
# if age < 0:
#     raise Exception("Age cannot be negative.")
# elif age < 18:
#     print("You are a minor.")
# else:
#     print("You are an adult.")


# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional Part as Answer
#         result = x // y
#         print("Yeah ! Your answer is :", result)
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")

# # Look at parameters and note the working of Program
# divide(32, 2)



try: 
    k = 15//3 # raises divide by zero exception. 
    print(k)      
except ZeroDivisionError:    
    print("Can't divide by zero") 
       
finally: 
    print('This is always executed') 