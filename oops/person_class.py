class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        if isinstance(name, str) and name:
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer.")
