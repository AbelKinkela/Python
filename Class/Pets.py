class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)
    
    def make_sound(self):
        print("Meow Meow Meow")

class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)
    
    def make_sound(self):
        print("w wow wow wow")


def my_pet(pet):
    pet.info()
    pet.make_sound()

if __name__ == "__main__":

    p1 = Cat("Happy", 3)
    p2 = Dog("Bobby", 2)
    print("PETS DETAILS:")
    my_pet(p1)
    print("----------------")
    my_pet(p2)


