#Q1 - Canine Class.
print()
class Canine:
    '''A canine class.'''
    attr1="mammal" #Our first attribute.
    attr2="dog"    #Our second attribute.
    #Our first sample method.
    def fun(self):
        print(f"I'm a {self.attr1}, and I'm a {self.attr2}.")
#Driver code:
Roger=Canine()
#Accessing class attributes.
print(f"I'm a {Roger.attr1}, and I'm a {Roger.attr2}.")
#Using our method.
Roger.fun()
#-------------------------------------------------------------------------------
#Q2 - Car Class.
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
#Q3 - Vehicle and Car Classes:
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
#-------------------------------------------------------------------------------
#Q4 - Reading and writing to a file.
print()
filename='ShallIDiePoemByShakespeare.txt'
#The with keyword automatically closes our file once access to it is
#no longer needed. The open() function returns an object representing
#our file. We use the as keyword to create an alias for our file object.
with open(filename,'r') as file_object:
    contents=file_object.read()
    print(contents.rstrip())
#Writing to a file. We specify a second argument 'w' to indicate that
#we'd like to write to our file. The first argument in open() is the
#name of the file we're writing to.
with open(filename) as file_1, open('Copy.txt','w') as file_2:
    file_2.write("This is a copy of the poem.\n\n")
    for line in file_1:
        file_2.write(line)
#-------------------------------------------------------------------------------
#Q5 - Example of exception handling.
print()
cookies=int(input("Enter the number of cookies you have as an integer: "))
people=int(input("Enter the number of people that will share these cookies: "))
#Our try-except block to handle division by 0.
try:
    #We try to divide our cookies by the number of people there are.
    cookies/=people
    print(f"Each person will get {cookies} cookies.")
#If we have a division by 0 error:
except ZeroDivisionError:
    print("You can't divide by 0! There has to be atleast 1 person...")



