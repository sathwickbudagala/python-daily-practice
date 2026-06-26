class Employee:
    def __init__(self, name, base_salary, bonus):
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus

    def total_salary(self):
        return self.base_salary + self.bonus

    def introduce(self):
        print(self.name, self.total_salary())     

'''
- Class: Employee
- attributes: name, base_salary, bonus
- methods:
    total_salary() → base + bonus
    introduce()    → prints name and total salary
'''