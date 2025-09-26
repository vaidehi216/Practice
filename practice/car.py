# n = int(input("Enter the year:"))
# class Car:
#     def __init__(self, brand, model, year, milage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.milage = milage

#     def car_information(self):
#         print(f"carbrand : {self.brand}")
#         print(f"carmodel : {self.model}")
#         print(f"year : {self.year}")
#         print(f"milage : {self.milage}")

# cars = [
#     Car("xuv", "3x0", "2025", "1000"),
#     Car("toyota", "corolla", "2020", "20000"),
#     Car("ford", "focus", "2018", "35000"),
#     Car("nexon","fearless","2024","40000")
# ]

# for car in cars:
#     car.car_information()
#     print("---")
# else:
#     print("No car found")


# ------------------------------------------------------


# n = int(input("Enter the year:"))
# class Car:
#     def __init__(self, brand, model, year, milage):
#         self.brand = brand
#         self.model = model
#         self.year = int(year)
#         self.milage = milage

#     def car_information(self):
#         print(f"carbrand : {self.brand}")
#         print(f"carmodel : {self.model}")
#         print(f"year : {self.year}")
#         print(f"milage : {self.milage}")

# cars = [
#     Car("xuv", "3x0", "2025", "1000"),
#     Car("xuv", "3x0", "2025", "1000"),
#     Car("toyota", "corolla", "2020", "20000"),
#     Car("ford", "focus", "2018", "35000"),
#     Car("nexon","fearless","2024","40000")
# ]

# matched_cars = [car for car in cars if car.year == n]
# if matched_cars:
#     for car in matched_cars:
#         car.car_information()
#         print("---")
# else:
#     print("No car found for the entered year.") 


# -----------------------------------------------------



# roll_no = int(input("Enter the roll number: "))

# class Student:
#     def __init__(self, roll_no, name, marks):
#         self.roll_no = roll_no
#         self.name = name
#         self.marks = marks  

#     def total_marks(self):
#         return sum(self.marks.values())

#     def student_information(self):
#         print(f"Roll No: {self.roll_no}")
#         print(f"Name: {self.name}\n")
#         print("Marks:")
#         for subject, score in self.marks.items():
#             print(f"  {subject}: {score}")
#         print(f"Total Marks: {self.total_marks()}")

# students = [
#     Student(1, "vaidehi", {"Math": 85, "Science": 90, "English": 88}),
#     Student(2, "kenita", {"Math": 78, "Science": 82, "English": 80}),
#     Student(3, "Charmi", {"Math": 92, "Science": 88, "English": 91}),
#     Student(4, "Devika", {"Math": 70, "Science": 75, "English": 72}),
# ]

# matched_students = [student for student in students if student.roll_no == roll_no]
# if matched_students:
#     for student in matched_students:
#         student.student_information()
#         print("---")
# else:
#     print("No student found for the entered roll number.")


# ---------------------------------------------------------


roll_no = int(input("Enter the roll number: "))

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  

    def total_marks(self):
        return sum(self.marks.values())

    def student_information(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}\n")
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"  {subject}: {score}")
        print(f"Total Marks: {self.total_marks()}")

students = {
    1: Student(1, "vaidehi", {"Math": 85, "Science": 90, "English": 88}),
    2: Student(2, "kenita", {"Math": 78, "Science": 82, "English": 80}),
    3: Student(3, "Charmi", {"Math": 92, "Science": 88, "English": 91}),
    4: Student(4, "Devika", {"Math": 70, "Science": 75, "English": 72})
}

student = students.get(roll_no)
if student:
    student.student_information()
else:
    print("No student found for the entered roll number.")
