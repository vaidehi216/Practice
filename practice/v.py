# a = "Hello"
# b = "World"

# print(a, b)   
# print(a, b, end="")  
# print(a, b, sep="&") 
# print(a, b, sep="") 


# a = "Hello"
# n = 5
# print(a * n)

# s = "Hello", n = 20, f = 5.5
# f = float(input().strip())
# print(f * 10)


# n = 4
# for i in range(1 ,n +1):
#     for j in range(1, i + 1):
#         print("*", end='')
#     print()

# astring = "Hello      !"
# afewwords = astring.strip(" ")
# print(afewwords)
# 


# class MyClass:
#     variable = "blah"

#     def function(self):
#         print("This is a message inside the class.")

# myobjectx = MyClass()

# myobjectx.variable
# myobjectx.function()
# print(myobjectx.variable)



# def fib():
#     a, b = 1, 1
#     while 1:
#         yield a
#         a, b = b, a + b

# # testing code
# import types
# if type(fib()) == types.GeneratorType:
#     print("Good, The fib function is a generator.")

#     counter = 0
#     for n in fib():
#         print(n)
#         counter += 1
#         if counter == 20:
#             break


# text = "hi    hello   how   are   you"
# cleaned = text.replace(" ", "")
# print(cleaned)


# text = "hi hello how are you"
# cleaned = "".join(text.split())
# print(cleaned)


count = 0
count += 4
count *= 2
count -= 1

print(f"count = {count}")