class Dog:

    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    philo = Dog("Philo", 5)
    mikey = Dog("Mikey", 6)

    print(f"{philo.name} is {philo.age} and {mikey.name} is {mikey.age}")

    if philo.species == "mammal":
        print(f"{philo.name} is a {philo.species}")
