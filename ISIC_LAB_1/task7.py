class Dog:
        def __init__(self, name, age, color):
            self.name = name
            self.age = age
            self.color = color

        def sound(self):
            print(f"{self.name} is barking!")

dog1 = Dog("Burek", 13, "czarnuch")
dog1.sound()