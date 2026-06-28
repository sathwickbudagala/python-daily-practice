class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Dog(Animal):
    def __init__(self):
        super().__init__("dog","woof")
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Cat(Animal):
    def __init__(self):
        super().__init__("cat","meow")
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Cow(Animal):
    def __init__(self):
        super().__init__("cow","ambaaa")
    def speak(self):
        print(f"{self.name} says {self.sound}")
'''
- Parent class: Animal
    - attributes: name, sound
    - method: speak() → "Dog says Woof"

- Child classes: Dog, Cat, Cow
    - each overrides speak() with their own sound
    '''