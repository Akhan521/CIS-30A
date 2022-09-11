#Q1: Working with a list.
planets=['Earth','Moon','Venus','Mars','Mercury','Saturn']
#a) Printing the list.
print(planets)
#b) Printing planet at index 4.
print(planets[4])
#c) Printing planets from indices 2-4.
print(planets[2:5])
#d) Printing the first 3 items.
print(planets[:3])
#e) Appending or Inserting Jupiter.
planets.append('Jupiter')
#planets.insert(6,'Jupiter')
print(planets)
#f) Sorting the list.
planets.sort()
print(planets)
#g) Seeing if Pluto is in our list.
print('Pluto' in planets)
#h) Sorting in reverse order.
reversed_planets=sorted(planets)
reversed_planets.reverse()
print(reversed_planets)
#i) Deleting Moon using pop or del.
del planets[4]
#planets.pop(4)
print(planets)
#j) Printing the length of our list.
print(len(planets))
#k) Using sort vs. sorted on a list of fruits.
fruits=['Strawberry','Apple','Orange','Mango',
        'Peach','Banana','Watermelon','Grapes']
sorted_fruits=sorted(fruits)
print(sorted_fruits)
fruits.sort()
print(fruits)
#l) Adding 2 lists together.
list1=[10,20,30,40,50,60]
list2=['Strawberry','Apple','Orange','Mango',
       'Peach','Banana','Watermelon','Grapes']
print(list1+list2)
