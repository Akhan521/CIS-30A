#Q1: Working with a list of planets.
print('''
Working with a list of planets:
-------------------------------''')
#a) Creating and printing our list.
planets=['Earth','Moon','Venus','Mars','Mercury']
print(planets)
#b) Printing the 4th planet.
print(planets[3])
#c) Printing planets 2-4.
print(planets[1:4])
#d) Adding Jupiter to the end.
planets.append('Jupiter')
print(planets)
#e) Sorting the list.
planets.sort()
print(planets)
#f) Seeing if the Sun is in our list.
print('Sun' in planets)
#g) Sorting in reverse order.
planets.sort()
planets.reverse()
print(planets)
#h) Determining the length of our list.
print(len(planets))
#i) Adding Jupiter to the beginning of our list.
planets.insert(0,'Jupiter')
print(planets)
#j) Removing the last planet using pop().
planets.pop()
print(planets)
#k) Deleting the first planet using del.
del planets[0]
print(planets)
#l) Removing Mars using remove().
planets.remove('Mars')
print(planets)
print()
#-------------------------------------------------------------------------------
#Q2: Working with arrays.
print('''
Working with arrays:
--------------------''')
#a) Importing numpy.
import numpy as np
#b) Creating our first array.
array1=np.array([11,22,33,44])
print(array1)
#c) Creating our second array with 777 in the beginning.
#   We insert 777 at the front of array1 and store it in array2.
array2=np.insert(array1,0,777)
#array2=np.array([777,11,22,33,44])
print(array2)
#d) Creating our third array with 555 in the beginning and 999 at the end.
#   We insert 555 at the front of array1 and 999 at the end of array1.
array3=np.insert(array1,0,555) #Adding 555 to the front.
array3=np.append(array3,999)   #Appending 999 to the end.
#array3=np.array([555,11,22,33,44,999])
print(array3)
print()
#-------------------------------------------------------------------------------
#Q3: Checking account problem.
print('''
Checking account problem:
-------------------------''')
checking_balance=1000
saving_balance=1500
if(checking_balance<2000):
    checking_balance+=500
    saving_balance-=500
print("Checking Balance = ",checking_balance)
print("Saving Balance   = ",saving_balance)
print()
#-------------------------------------------------------------------------------
#Q4: Age problem.
print('''
Printing messages based on your age:
------------------------------------''')
age=int(input("Enter your age: "))
if(age<21):
    print("Illegal drinking age!")
elif(age>65):
    print("Eligible for Medicare!")
else:
    print("Keep working!")
print()
#-------------------------------------------------------------------------------
#Q5: Comparing 2 numbers.
print('''
Comparing 2 numbers:
--------------------''')
num1=int(input("Enter the first number to compare: "))
num2=int(input("Enter the second number to compare: "))
print()
if(num1==num2):
    print("Numbers 1 and 2 are the same.")
elif(num1<num2):
    print("Number 1 is smaller than Number 2.")
else:
    print("Number 1 is larger than Number 2.")
print()
#-------------------------------------------------------------------------------
#Q6: Printing different messages based on input.
print('''
Printing messages based on user input:
--------------------------------------''')
choice=input("Enter either 1 or 2: ")
if(choice=='1'):
    print("Hello World!")
elif(choice=='2'):
    print("Python Rocks!")
else:
    print("You did not enter a valid number.")
print()    
#-------------------------------------------------------------------------------
#Q7: Perfect numbers problem.
#    Perfect numbers: 6, 28, 496, 8128, 33550336.
print('''
Checking if we have a perfect number:
-------------------------------------''')
num=int(input("Enter an integer: "))
if(num==6):
    print("That's a perfect number!")
elif(num==28):
    print("That's a perfect number!")
elif(num==496):
    print("That's a perfect number!")
elif(num==8128):
    print("That's a perfect number!")
elif(num==33550336):
    print("That's a perfect number!")
else:
    print("That is NOT a perfect number!")
print()
#-------------------------------------------------------------------------------
#Q8: Even and odd problem.
print('''
Checking if a number is even or odd:
------------------------------------''')
num=int(input("Enter an integer: "))
#If it's evenly divisible by 2, then it's even.
if(num%2==0):
    print(num,"is an even integer.")
#Otherwise, it's odd.
else:
    print(num,"is an odd integer.")
print()
#-------------------------------------------------------------------------------
#Q9: Dictionary of scores problem.
print('''
Dictionary of scores problem:
-----------------------------''')
scores={'Rick Sanchez': 70, 'Morty Smith': 35,
        'Summer Smith': 82, 'Jerry Smith': 23,
        'Beth Smith': 98}
#Checking each student's score:
for student in scores:
    #If the score is >=65, the student passed the class.
    if(scores[student]>=65):
        print(f"{student} passed the class with {scores[student]}%!")
    else:
        print(f"{student} failed the class with {scores[student]}%.")
print()
