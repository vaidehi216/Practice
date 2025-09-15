# class student:
#     name = "karan"

# s1 = student()
# print(s1.name)  


# class student:
#     collage_name = "ABC University"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("adding student details")
    
# s1 = student("Karan", 20)
# print(s1.name)  


# @staticmethod
# def hello():
#     print("Hello, this is a static method!")
# print(hello())  


# class student:
#     def __init__(self, che, phy, math):
#         self.che = che
#         self.phy = phy
#         self.math = math

#     @property
#     def percentage(self):    
#         return str((self.che + self.phy + self.math) / 3) + "%"

# student1 = student(89, 97, 99)
# print(student1.percentage)

# student1.phy = 90
# print(student1.percentage)


# @getattr
# @setattr
# @delattr
# @property



# class student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def calc_average(self):
#         sum = self.marks1 +self.marks2 + self.marks3
#         get_avg = sum/3
#         return get_avg
# obj = student("Aditya",99,98,97)
# print("hello",obj.name,"your avg marks is ",obj.calc_average())


# class complex:
#     def __init__(self, real, imag):
#         self.real = real     
#         self.imag = imag
    
#     def shownum(self):
#         print(f"{self.real} + {self.imag}i")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImag = self.imag + num2.imag
#         return complex(newReal, newImag)     
    
# num1 = complex(1, 3)
# num1.shownum()

# num2 = complex(4, 5)
# num2.shownum()

# num3 = num1 + num2
# num3.shownum()


# def stands for define. #It is used to create (define) a function. #Functions are blocks of code that run when you call them.
# self vairable is used to refer to the instance of the class itself.
# self is used to access variables that belong to the class.
#__init__ is a special method that is automatically called when an object of the class is created. It initializes the object's attributes.
#return Send a value back to the caller (outside the function)  #Exit the function
#dunder functions (__init__,__add__, __str__, etc.) 



class employee:
    def __init__(self, dep, rol, salary):
        self.dep = dep
        self.rol = rol
        self.salary = salary    
    
    def show_details(self):
        print(f"Department: {self.dep}, Role: {self.rol}, Salary: {self.salary}")

class engineer(employee):
        def __init__(self, name, age):
            self.name = name
            self.age = age
            super().__init__("Engineer", "it", "70,000")

enng1 = engineer("Alice", 30)
enng1.show_details() 