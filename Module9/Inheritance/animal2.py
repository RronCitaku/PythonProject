class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound")

    def describe(self):
        print(f"This is {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Woof! Woof!")

    def describe(self):
        super().describe()
        print(f"Breed: {self.name}.")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Meow! Meow!")

    def describe(self):
        super().describe()
        print(f"Color: {self.color}.")

animal = Animal("Animal")
animal.sound()
animal.describe()

dog = Dog("Rex", "Golden Retriever")
dog.sound()
dog.describe()

cat = Cat("Whiskers", "Black")
cat.sound()
cat.describe()