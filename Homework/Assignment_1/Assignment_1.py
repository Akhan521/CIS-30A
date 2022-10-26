#Q1 - Cities list:
#Q1.a: Creating a list of cities.
cities=['San Francisco', 'Los Angeles', 'Portland', 'Seattle',
        'New York', 'Boston', 'Chicago', 'St.Louis', 'Dallas']
print(cities)
print() #Newline.
#Q1.b: Sorting the list.
cities.sort()
print(cities)
print()
#Q1.c: Printing the 4th city.
print(cities[3])
print()
#Q1.d: Printing cities 2-4.
print(cities[1:4])
print()
#Q1.e: Adding a city.
cities.append('Cincinnati')
print(cities)
print()
#Q1.f: Seeing if Miami is in our list.
print('Miami' in cities)
print()
#Q1.g: Sorting in reverse order.
cities.sort()
cities.reverse()
print(cities)
print()
#Q1.h: Printing the length.
print(len(cities))
print()
#Q1.i: Adding a city to the beginning.
cities.insert(0,'Denver')
print(cities)
print()
#-------------------------------------------------------------------------------
#Q2 - Switching the 1st letters of names:
first=input("Please enter your first name: ")
last =input("Please enter your last name: ")
print()
#We take the first letter of the last name and print the rest of the first name.
#We take the first letter of the first name and print the rest of the last name.
#I used string concatenation because it made the most sense for me to use.
print(f"Your new name is {last[0]+first[1:]} {first[0]+last[1:]}.")
print()
#-------------------------------------------------------------------------------
#Q3 - Area of a rectangle:
length=float(input("Enter the length of the rectangle as a float: "))
height=float(input("Enter the height of the rectangle as a float: "))
area=length*height
print()
print(f"The area of the rectangle = {area:.2f}")
print()
#-------------------------------------------------------------------------------
#Q4 - Converting inches to feet.
inches=int(input("Enter the number of inches as an integer: "))
feet=int(inches/12) #We divide by 12 to get our feet (We need it as an int).
inches=inches%12    #We get the remainder of inches/12 as our inches.
print(f"You have {feet} feet, {inches} inches.")
print()
#-------------------------------------------------------------------------------
#Q5 - Printing that the year 2020 + Age will be a great year:
name=input("Please tell me your name: ")
age=int(input(f"How old are you, {name}? "))
print()
print(f"Then, {2020+age} will be your year!")
print()
#-------------------------------------------------------------------------------
#Q6 - Converting from degrees to radians: 360 degs = 2 pi radians.
pi=3.1415
degrees=int(input("Enter the number of degrees as an integer: "))
radians=degrees*(pi/180)
print(f"{degrees} degrees = {radians:.4f} radians.")
print()
#-------------------------------------------------------------------------------
#Q7 - Printing the middle character of a string w/ an odd number of letters.
myString=input("Enter a string with an odd number of letters: ")
middle=int(len(myString)/2) #Finding the middle of our string.
print("The middle character is: ", myString[middle])
print()
#-------------------------------------------------------------------------------
#Q8 - Dictionary of countries to their capitals:
cntry_cap={'USA':'Washington D.C','United Kingdom':'London',
           'China':'Beijing','Japan':'Tokyo','France':'Paris'}
print(cntry_cap)
print()
#a. Deleting the third country from our dict.
del cntry_cap['China']
print(cntry_cap)
#b. Adding a country to our dict.
cntry_cap['Germany']='Berlin'
print(cntry_cap)
print()
#-------------------------------------------------------------------------------
#Q9 - Printing a multiline string:
print('''Date:\nDecember 25, 2022\n
Time:\n11:50 PM\n
Venue:\nConvention Center\n
Number of guests:\n200\n''')
#-------------------------------------------------------------------------------
#Q10 - Using format() and placeholders with a string:
laptop='Apple'
price=1299
ex_rate=1.320
print('''The price of this {0:s} laptop is {1:d} USD, and the
exchange rate is 1 USD to {2:1.3f} Canadian dollars.'''
.format(laptop,price,ex_rate))
