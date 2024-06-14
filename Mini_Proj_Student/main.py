class Student:
    
    def __init__(self, name, age):
    
        self.name = name
    
        self.age = age
    
        self.grades = []

    def add_grade(self, grade):
    
        self.grades.append(grade)

    def display_info(self):

        print(f"Name: {self.name}")

        print(f"Age: {self.age}")

        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):

        if not self.grades:

            return "No grades available."

        return sum(self.grades) / len(self.grades)

students_database = []

def add_student_to_database(name, age, grades=None):

    if grades is None:

        grades = []

    new_student = Student(name, age)

    for grade in grades:

        new_student.add_grade(grade)

    students_database.append(new_student)

add_student_to_database("jimmy", 22, [87,90,92])

add_student_to_database("cooper", 24, [78,85,80])

add_student_to_database("kasra", 28, [95,88,90])

for student in students_database:

    student.display_info()

    avg_grade = student.calculate_average_grade()

    print(f"Average Grade: {avg_grade}")