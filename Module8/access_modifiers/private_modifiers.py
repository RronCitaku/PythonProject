class myclass:

    def __init__(self):
        self.__private_variable = "This is my private variable"

    def __private_method(self):
        print("This is my private method")

my_class = myclass()
print(my_class.__private_variable)
my_class.__private_method()