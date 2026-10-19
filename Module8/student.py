class Student:
    school_name = "Digital School"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Rroni", 17, "Python")
student2 = Student("Yllka", 22, "PHP")
print(student1.school_name)
print(student2.school_name)
