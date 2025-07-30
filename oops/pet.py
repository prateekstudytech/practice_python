class Pet:

    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
    
    def get_name(self):
        return self.__name
    
    def get_breed(self):
        return self.__breed
    
    def __str__(self):
        print(f"Pet name = {self.get_name()} and breed = {self.get_breed()}")


