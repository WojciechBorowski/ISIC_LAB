class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Meow!"

class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sound(self):
        return "(fox sounds)!"
