class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def who(self):
        print(f"my name is {self.name} and my age is {self.age}")
s=Student("sunny",21)
print(s.who())