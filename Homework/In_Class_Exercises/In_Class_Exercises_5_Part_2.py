#Q1 - Car Class.
print()
class Car:
    '''A car class.'''
    #Our class attribute.
    wheels=4
    #Our init method.
    def __init__(self,color,style):
        #Our instance attributes.
        self.color=color
        self.style=style
    #Our show description method.
    def showDescription(self):
        print(f"This car is a(n) {self.color} {self.style}.")
    #Our change color method.
    def changeColor(self,color):
        self.color=color
#Driver code:
c=Car("Black","SUV")
#Accessing our attributes.
print(f"This car is a(n) {c.color} {c.style}.")
#Modifying our style attribute.
c.style="Sedan"
print(f"This car is a(n) {c.color} {c.style}.")
#Using our change color and show description methods.
c.changeColor("Blue")
c.showDescription()
#-------------------------------------------------------------------------------
#Q2 - Vehicle and Car Classes:
print()
#Our base class.
class Vehicle:
    '''Our base class.'''
    #A sample method.
    def showDescription(self):
        print("I'm a vehicle.")
    def setSpeed(self,speed):
        print(f"Now, you're traveling at {speed} mph.")
#Our derived class.
class Car(Vehicle):
    '''Our derived class.'''
    #A sample method.
    def showDescription(self):
        print("I'm a car.")
#Driver code:
v=Vehicle()
c=Car()
#Using our methods.
v.showDescription()
c.showDescription()
#Using our set speed method.
c.setSpeed(25)
