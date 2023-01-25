#Q1 - Vehicle class.
print()
class Vehicle:
    #Our init method.
    def __init__(self,name,color,kind,value):
        self.name=name
        self.color=color
        self.kind=kind
        self.value=value
    #Our show description method.
    def showDesc(self):
        print(f"This {self.name} is a {self.color} {self.kind} worth ${self.value:.2f}.")
#Driver code:
car1=Vehicle("BMW","red","convertible",60000)
car2=Vehicle("Chevy","blue","van",10000)
#Printing our descriptions.
car1.showDesc()
car2.showDesc()
