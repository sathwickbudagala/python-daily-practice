class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(3.14*(self.radius)**2)
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)

'''
- Class: Circle   → area using radius
- Class: Rectangle → area using length x width
- Both should have a method called area()
'''