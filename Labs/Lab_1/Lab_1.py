#Q1 - A bunch of different operations:
#Q1.a
print("Hello Kitty")
print()

#Q1.b
print(10+5)
print()

#Q1.c -> 13**7 = 62748517. This is the exponentiation operator.
print(13**7)
print()

#Q1.d -> 13**7 and 13^7 have the different results. The ** operator
#is the exponentiation operator. The ^ operator is the XOR operator.
#It returns a 1 if both bits are different. Otherwise, it returns a 0.
#13=1101 and 7=0111 in binary. Then, 13^7=1101^0111=1010=10. The first and
#third bits of both are different, so we have 1's there and 0's elsewhere.
print(13^7) #We should expect to get 10 in decimal.
print()

#Q1.e -> -7//2 = -4
print(-7//2) #The // operator performs floor division.
print()

#Q1.f -> 20 - 360 + 156 = 184
print(20 - 10 * 36 + 3 * 52)
print()

#Q1.g -> 3.1415 = 3 when converted to an integer
print(int(3.1415))
print()

#Q1.h -> 30>=30 = True
print(30>=30)
print()

#Q1.i - String operations:
name = "DonaldDaisyDuck"
print(name)
print(name[4])      #5th character
print(name[3:9])    #4-9th characters
print(name.upper())
print(name * 3)
print()

#Q1.j - Arithmetic: 493 * 13 = 6409
mickey=124
minnie=369
print((mickey+minnie) * 13)
print()

#Q1.k - % vs. and
a=8
b=10
print(a & b)   #8=1000 & 10=1010 in binary, then a & b = 1000 or 8. The & operator
               #returns a 1 if both values are 1. Otherwise, a 0 is returned.
               #Only the first number in both are both 1, so a 1 is returned.
               #All other values return a 0 because they aren't both 1's.
print(a and b) #The and operator checks the first value which is 8. Since, it is
               #nonzero, it is true. It then checks 10, which again is true because
               #it is nonzero. The last true value is returned, so the 10 is returned.
print()

#Q1.l - Bitwise Shifting
x=3
x>>=5    #3 is 0000 0011 in binary. We're performing a right shift of 5 bits, so
         #we end up with 0000 because by the time we shift it 2 bits to the right,
         #we already get 0. Shifting it another 3 bits doesn't change the fact
         #that we still end up with a 0.
print(x)
print()

#Q1.m -> Adding 2 integers
num1 = input("Enter integer 1: ")
num1 = int(num1)
num2 = input("Enter integer 2: ")
num2 = int(num2)
print(f"The sum is: {num1+num2}")
print()

#Q1.n - Embedding values:
myScore=85
message="I scored %s points."
print(message % myScore)
print()

#Q1.o -> Adding any 2 numbers (not only integers):
num1 = input("Enter number 1: ")
num1 = float(num1)
num2 = input("Enter number 2: ")
num2 = float(num2)
print(f"The sum is: {num1+num2}")
print()

#Q1.p - Finding the mean and median:
import statistics
print("Enter 3 numbers in sorted order.")
num1 = input("Enter number 1: ")
num1 = float(num1)
num2 = input("Enter number 2: ")
num2 = float(num2)
num3 = input("Enter number 3: ")
num3 = float(num3)
print("Number 1: ", num1)
print("Number 2: ", num2)
print("Number 3: ", num3)
print("The mean is:   ", statistics.mean([num1,num2,num3]))
print("The median is: ", statistics.median([num1,num2,num3]))
print()

#Q1.q - Conditional statement:
age = 14
if(age>12 and age<20):
    print("You are a teenager.")
    print()
    
#Q1.r - Set property:
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] #10 elements in a.
b = set(a) #4 elements because duplicates aren't allowed.
print(len(a) - len(b)) #10-4 = 6. len(a)=10 and len(b)=4.
print()

#Q1.s -> Creating a dictionary. Key=Name of City. Value=Population in millions.
population = {'Shanghai':17.8,'Istanbul':13.3,
              'Karachi':13.0,'Mumbai':12.5} 
print(population.keys())
print() #Printing a newline to make space.
#------------------------------------------------------------------------------
#Q2 - Sum of 3 user-entered numbers:
print("Calculating the sum of 3 numbers:")
num1 = input("Enter the first number:  ")
num1 = float(num1)
num2 = input("Enter the second number: ")
num2 = float(num2)
num3 = input("Enter the third number:  ")
num3 = float(num3)
message="The sum is: %s"          #Formatted string.
print(message % (num1+num2+num3)) #Embedding the sum into a string.
print()
#------------------------------------------------------------------------------
#Q3 - Sum of 5 user-entered numbers:
print("Calculating the sum of 5 numbers:")
num1 = input("Enter the first number:  ")
num1 = float(num1)
num2 = input("Enter the second number: ")
num2 = float(num2)
num3 = input("Enter the third number:  ")
num3 = float(num3)
num4 = input("Enter the fourth number: ")
num4 = float(num4)
num5 = input("Enter the fifth number:  ")
num5 = float(num5)
sum=num1+num2+num3+num4+num5 #Storing the sum
print("The sum is: ",sum)
print()
#-------------------------------------------------------------------------------
#Q4 - Sum of any number of numbers:
sum=0 #To hold the sum.
size=int(input("How many numbers do you want to sum? "))
#Loop for as many numbers we want to sum.
for i in range(size): 
    num = input(f"Enter number {i+1}:  ")
    num = float(num)
    sum+=num
print("The sum is: ",sum)
print()
#-------------------------------------------------------------------------------
#Q5 - Average of any number of numbers:
result=0 #To hold the result.
size=int(input("How many numbers do you want to average? "))
#Loop for as many numbers we want to sum.
for i in range(size): 
    num = input(f"Enter number {i+1}:  ")
    num = float(num)
    result+=num
#Divide the sum by the size to get the average:
result/=size
print("The average is: ",result)
print()
#-------------------------------------------------------------------------------
#Q6 - Median of 5 numbers:
print("Enter 5 numbers in sorted order and the median will be found.")
num1 = input("Enter number 1: ")
num1 = float(num1)
num2 = input("Enter number 2: ")
num2 = float(num2)
num3 = input("Enter number 3: ")
num3 = float(num3)
num4 = input("Enter number 4: ")
num4 = float(num4)
num5 = input("Enter number 5: ")
num5 = float(num5)
result="The median is: %s" % statistics.median([num1,num2,num3,num4,num5])
print(result)
print()
#-------------------------------------------------------------------------------
#Q7 - Drawing a shape using Python Turtle:
import turtle
#Moving the turtle to a different position:
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
#Setting the fill color:
turtle.fillcolor('PaleGreen')
#The start of our filling operation:
turtle.begin_fill()
#Drawing an octagon:
for i in range(8):
    turtle.forward(100)
    turtle.right(45)
#The end of our filling operation.
turtle.end_fill()
    
           

