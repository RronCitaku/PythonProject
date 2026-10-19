class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}, I am {self.age} years old!")

person1 = Person("Rroni", 18)
person2 = Person("Filan", 20)

person1.greet()
person2.greet()