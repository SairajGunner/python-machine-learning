from animal import Animal

class Human(Animal):
    def __init__(self, alive, name, age):
        super().__init__(alive, "Human", name, age)

    def work(self):
        print(f"{self.type.capitalize()} named {self.name} is working.")

    def sleep(self):
        print("Humans do not sleep.")

animal = Animal(True, "Lion", "Leo", 7)
animal.sleep()

human = Human(True, "Lionel", 20)
human.work()
human.sleep()