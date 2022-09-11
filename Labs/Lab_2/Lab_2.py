#Q1: Creating a list of carmakers.
cars=['BMW','Chrysler','Ford','GM','Honda',
      'Hyundai','Kia','Mercedes','Nissan','VW']
#a) Printing the list.
print(cars)
#b) Printing item at index 1.
print(cars[1])
#c) Starting at index 3 and ending at index 7 with a step of 4.
#   This allows us to only output the items at index 3 and 7.
print(cars[3:8:4])
#d) Printing first 3 items.
print(cars[:3])
#e) Explaining why print(cars[-1]) outputs VW:
#   Indexing starts at 0 and it goes until 1 less than the size
#   of the list. However, we also can use negative indexing.
#   Negative indexing allows us to look at our elements from the end.
#   This would begin from -1 and go till -size of the list. This is why
#   cars[-1] is accessing the last carmaker in our list and printing it.
#f) Adding a car to our list.
cars.append('Tesla')
#g) Inserting a car at a specific index.
cars.insert(3,'Porsche')
#h) Removing an item from our list.
del cars[9]       #Deleting Nissan from our list.
# cars.remove('Nissan') would also remove Nissan.
#i) Sorting our list.
cars.sort()
#j) Repeating our list 3 times.
print(cars * 3)
#k) Printing the length.
print(len(cars))
#l) Using sort vs sorted.
sorted_cars=sorted(cars)  #Makes the data appear in sorted order, but it
                          #doesn't actually sort the original data.
cars.sort()               #Sorts the original data (Permanently).
#m) Reversing our list.
cars.reverse()
#n) Creating a tuple to hold perfect numbers.
perfectNumbers=(6,28,496,8128,33550336)
#o) Trying to add 2 to our tuple.
#   perfectNumbers.append(2) -> This wouldn't work
#   because a tuple is immutable, so adding isn't possible.
#-------------------------------------------------------------------------------
#Q2: Creating a list of countries to turn into a set.
countries = ['Canada', 'USA', 'Mexico', 'France',
             'Germany', 'UK', 'Russia', 'China',
             'Japan', 'Korea', 'South Africa', 'UAE',
             'India', 'Australia', 'India', 'Brazil']
#a) Printing how many countries are in our list.
print(len(countries))
#b) Determining the lenth of the set we'll be creating.
#   India repeats itself once in the list, so if we create a set from the list,
#   it should have 1 less item. In other words, our set will have
#   len(countries) - 1 elements because the duplicate of India will disappear.
#c) Printing countries from index 0 to 4.
print(countries[:5])
#d) Sorting the countries.
countries.sort()
#e) Creating a set and naming it country_set.
country_set=set(countries)
#f) Adding a country.
country_set.add('Ghana')
#g) Determining if Argentina is in the set using the in keyword.
#   If Argetina is in our set, true will be outputted. If it isn't,
#   false will be outputted. The in keyword is used to test this.
print('Argentina' in country_set)
#h) Printing the updated set.
print(country_set)
#i) Using pop(). The first country in our set is removed.
country_set.pop()
#-------------------------------------------------------------------------------
#Q3: Creating a dictionary.
totalMedalOlympic2016={'USA':121,'China':70,'GBR':67,'Russia':57,
                       'Germany':42,'France':42,'Japan':41,'Australia':29,
                       'Italy':28,'Canada':22,'Korea':21}
#a) Printing out our keys (countries).
for key in totalMedalOlympic2016:
    print(f"Country: {key}")
#b) Printing the value of each key (medal count).
for key in totalMedalOlympic2016:
    print("Medal Count: ",totalMedalOlympic2016[key])
#c) Adding a key-value pair. (Brazil:19)
totalMedalOlympic2016['Brazil']=19
#d) Printing our dictionary.
print(totalMedalOlympic2016)
#e) Determining if Poland is in our dictionary.
print('Poland' in totalMedalOlympic2016)
#f) Retrieving Poland's medal count if it exists.
#   If there is no medal count, we output a message letting us know.
print(totalMedalOlympic2016.get('Poland',"Medal count doesn't exist."))
#g) Using the identity operator (is) to check if Poland is present in our dict.
is_Present = totalMedalOlympic2016.get('Poland') #None is returned because
                                                 #Poland isn't in our dict.
isnt_Present = is_Present is None    #Checking to see if both are the same.
print(isnt_Present)                  #Printing true if Poland isn't in our dict.
#-------------------------------------------------------------------------------
#Q4: Creating an array.
import array as arr #Importing the array module.
import numpy as np  #Importing the numpy package.
array = np.array([6,28,496,8128]) #Creating an array.
#a) Dividing the array by 3 (Dividing each element by 3).
division = array / 3
#b) Adding 7 to the array (Adding 7 to each element).
addition = array + 7
#c) Multiplying the array by 13.
multiplication = array * 13
#d) Adding 144 to the end of our array.
new_Array = np.append(array,144)
#e) Removing 8128 from our array.
#   It is located at index 3.
new_Array = np.delete(array,3)
#f) Creating a list and attempting to divide by 3.
listPerfectNums = [6,28,496,8128]
# division = listPerfectNums / 3 -> We get an error when we execute
# this line of code. In order to divide each element in our list by 3,
# we'd have to individually divide each element. The same arithmetic
# that works on arrays doesn't work on lists. This is why we get an error.
#-------------------------------------------------------------------------------
#Q5: Drawing using Turtle.
import turtle
# Creating our pen object.
t = turtle.Pen()
# Postioning our pen.
t.penup()
t.goto(-100,150)
t.pendown()
# Drawing our 2 circles using a for loop.
for circle in range(2):
    # Draw the circle with a radius of 50.
    t.circle(50)
    # Moving to our next position for the next circle.
    t.penup()
    t.forward(150)
    t.pendown()
# Repostioning our pen for the next operation.
t.penup()
t.goto(-150,0)
t.pendown()
# Drawing 2 squares using a nested for loop.
# The outer loop handles the 2 squares, and the
# inner loop handles the 4 sides for each square.
for square in range(2):
    for side in range(4):
        t.forward(100)
        t.left(90)
    # Moving to our next position for the next square.
    t.penup()
    t.forward(150)
    t.pendown()  
# Repostioning our pen.
t.penup()
t.goto(-25,-150)
t.pendown()
# Drawing 1 more circle filled with red.
t.fillcolor('red') # Setting the fill color.
t.begin_fill()     # The start of our fill operation.
t.circle(50)       # Drawing our circle.
t.end_fill()       # The end of our fill operation.
