class Animal:
    def __init__(self, alive, animal_type, name, age):
        self.alive = alive
        self.type = animal_type
        self.name = name
        self.age = age

    def describe(self):
        print(f"Alive: {self.alive}\nType: {self.type.capitalize()}\nName: {self.name.capitalize()}\nAge: {self.age}")

    def eat(self):
        print(f"{self.type.capitalize()} named {self.name.capitalize} is eating.")

    def sleep(self):
        print(f"{self.type.capitalize()} named {self.name.capitalize()} is sleeping.")
