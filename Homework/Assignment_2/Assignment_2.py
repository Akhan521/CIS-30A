#Q1 - Sorting words:
print()
print("Question 1:")
s=input("Enter a string and its words will be sorted: ")
#Splitting the string into a list of words.
words_list=s.split()
#Sorting the list of words.
words_list.sort()
#Displaying the sorted words:
print("The sorted words are: ")
for word in words_list:
    print(word)
#-------------------------------------------------------------------------------
#Q2 - Using loops to display numbers:
print()
print("Question 2:")
x=46 #Assigning x between 40 and 50.
y=97 #Assigning y between 80 and 100.
#Looping under 2 conditions:
while(x<50 and y<100):
    #Incrementing both.
    x+=1
    y+=1
    #Displaying both.
    print(x,y)
#-------------------------------------------------------------------------------
#Q3 - Determing whether numbers are odd or even.
print()
print("Question 3:")
def isOdd(num):
    #If we have an odd number, we return true.
    if(num%2==1):
        return True
    #If we have an even number, we return false.
    else:
        return False
#Driver code:
num=int(input("Enter an integer and see if it's odd or even: "))
#Displaying if it's odd or even.
if(isOdd(num)):
    print(f"{num} is an odd integer.")
else:
    print(f"{num} is an even integer.")
#-------------------------------------------------------------------------------
#Q4 - Storing car information with a function:
print()
print("Question 4:")
#Our function requires 2 params and accepts an arbitrary # of keyword arguments.
def make_car(manufacturer,model_name,**kwargs):
    #Creating an empty dict to store our info.
    car_info={}
    #Storing the manufacturer.
    car_info['Manufacturer']=manufacturer
    #For every name-value pair we have, we store them.
    #The items() method returns a list of key-value pairs.
    for name,value in kwargs.items():
        #Storing each key-value pair.
        car_info[name]=value
    #Storing the model name.
    car_info['Model']=model_name
    #Returning our dict.
    return car_info
#Driver code:
car=make_car('Subaru', 'Outback', color='Blue', tow_package=True)
#Displaying our car's info.
print(car)
#-------------------------------------------------------------------------------
#Q5 - Calculating a sum:
print()
print("Question 5:")
def pSum(x,n):
    sum=1 #The sum starts with 1.
    #We iterate n times.
    for i in range(1,n+1):
        #We add x^i/i to our sum.
        sum+=(x**i/i)
    #We display our calculated sum.
    print(f"The sum of the series is = {sum:.2f}")
#Driver code:
x=2 #Assigning x.
n=5 #Assigning n.
#Calling our function.
pSum(x,n)
#-------------------------------------------------------------------------------
#Q6 - Calculating a product:
print()
print("Question 6:")
def pFact(k,m):
    product=k #The product starts with k.
    #We iterate m times.
    for i in range(1,m+1):
        #We multiply our product by k-i.
        product*=(k-i)
    #We return our calculated product.
    return product
#Driver code:
k=5 #Assigning k.
m=2 #Assigning m.
#If we have 2 positive integers:
if(k>0 and m>0):
    #Calculating and storing the product.
    product=pFact(k,m)
    #Displaying our product.
    print(f"The product of the series is = {product:d}")
#If we don't have 2 positive integers:
else:
    print("You have to enter 2 positive integers!")





