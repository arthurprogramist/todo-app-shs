class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = ""

    def make_sound(self):
        return self.sound


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "ruff ruff ruffff"

if __name__ == "__main__":
    dog = Dog("Bob")
    animal = Animal("Animal")
    print(dog.make_sound())