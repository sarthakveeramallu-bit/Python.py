from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name: {self.name}")
        print(f"Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")

class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")

class Lion(Animal):
    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride_size = pride
    def speak(self):
        print(f"{self.name} (Pride : {self.pride}) says: ROARRRRR!")

dog = Dog("Danger", "Home", "Tibetan Mastiff ")
parrot = Parrot("Polly", "Forest", "Falcon")
lion = Lion("Simba", "Savannah", "Tsavo Lions")

print("=== Animals Sound Show ===")
for animal in [dog, parrot, lion]:
    animal.display()
    animal.speak()
    print()