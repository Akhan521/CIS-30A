#Q1: Looping through a list.
print()
fruits=['Apple','Banana','Cherry']
#Printing all fruits.
for fruit in fruits:
    print(fruit)
#Printing all letters in Banana.
for letter in fruits[1]:
    print(letter)
#Printing all fruits using range().
for i in range(len(fruits)):
    print(fruits[i])
#Printing numbers:
for num in range(0,16,2):
    print(num)
#-------------------------------------------------------------------------------
#Q2: Using a while loop.
print()
limit=40
num=0
#Printing the square of num+1 as long as it's < limit.
while((num+1)**2 < limit):
    print(num+1,(num+1)**2)
    num+=1
#-------------------------------------------------------------------------------
#Q3: Difference between 2 addition operations.
print()
num1=input("Enter your 1st float: ")
num2=input("Enter your 2nd float: ")
#Printing the sum of the 2 floats. We have to first convert
#each input into a float because the input function stores
#input as a string.
print(float(num1)+float(num2))
#Here, we're adding 2 strings together, so this isn't the same
#as finding the sum of the 2 floats.
print(num1+num2)
