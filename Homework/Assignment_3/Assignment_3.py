#Q1 - Bank Account Class.
print()
print("Question 1: Bank Account Class\n")
class Bank_Account:
    #Our constructor.
    def __init__(self):
        print("Hello! Welcome to the deposit and withdrawal ATM.")
        self.balance=0
    #Our deposit method.
    def deposit(self):
        deposit=float(input("Enter the amount to be deposited: "))
        self.balance+=deposit
        print(f"Amount deposited: ${deposit:.1f}")
        print()
    #Our withdraw method.
    def withdraw(self):
        withdrawn=float(input("Enter the amount to be withdrawn: "))
        #If we are able to withdraw the amount, we do so.
        if(self.balance >= withdrawn):
            self.balance-=withdrawn
            print(f"You withdrew: ${withdrawn:.1f}")
        else:
            print("You have insufficient funds! You must have enough funds.")
        print()        
    #Our display method.
    def display(self):
        print(f"Net available balance = ${self.balance:.1f}")
#Driver code:
account=Bank_Account()
#Depositing some money.
account.deposit()
#Withdrawing some money.
account.withdraw()
#Displaying our net balance.
account.display()
#-------------------------------------------------------------------------------
#Q2 - Restaurant Class.
print()
print("Question 2: Restaurant Class\n")
class Restaurant:
    #Our constructor.
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
    #Our 1st method.
    def describe_Restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine}.")
    #Our 2nd method.
    def open_Restaurant(self):
        print(f"{self.name} is open. Come on in!")
#Driver code:
restaurant=Restaurant("The Mean Queen","pizza")
#Displaying our attributes individually.
print(restaurant.name)
print(restaurant.cuisine)
print()
#Calling our 2 methods.
restaurant.describe_Restaurant()
restaurant.open_Restaurant()
#-------------------------------------------------------------------------------
#Q3 - Ice Cream Stand Class.
print()
print("Question 3: Ice Cream Stand Class\n")
#Our class inherits from the restaurant class.
class IceCreamStand(Restaurant):
    #Our constructor.
    def __init__(self,name,cuisine):
        #Calling our super class's constructor.
        super().__init__(name,cuisine)
        #Our list of flavors.
        self.flavors=["Vanilla","Chocolate","Black Cherry"]
    #Our show flavors method.
    def showFlavors(self):
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")
#Driver code:
stand=IceCreamStand("The Big One","ice cream")
#Calling a derived method.
stand.describe_Restaurant()
print()
#Displaying our flavors.
stand.showFlavors()
    





    
