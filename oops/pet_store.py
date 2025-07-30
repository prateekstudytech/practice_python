from pet import Pet

class PetStore:
    def __init__(self, name):
        self.__stroreName = name
        self.__pets = []
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self.__pets.append(pet)
        else:
            raise ValueError("Only instances of Pet can be added.")

    def get_pets(self):
        return self.__pets
