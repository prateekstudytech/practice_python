class Dog:
    """
    This is a class for defining Dogs.



    Returns:
        Object of type Dog
    """

    species = "mammal"

    def __init__(self, name, age):
        """
        __init__ The constructor for Dog class

        Arguments:
            name -- Name of the dog
            age -- Age of the dog
        """
        self.name = name
        self.age = age
    
    def description(self):
        """
        description function to return description of Dog

        Returns: 
            string: Dog is x years old.
        """
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        """
        speak function to return greet sound by the dog

        Arguments:
            sound:str -- sound of the dog

        Returns:
            str: -- greet of the dog
        """
        return f"{self.name} says {sound}"
    
    def birthday(self):
        """
        birthday Increment age on the birthdays
        """
        self.age += 1

if __name__ == "__main__":
    philo = Dog("Philo", 5)
    mikey = Dog("Mikey", 6)

    print(mikey.description())
