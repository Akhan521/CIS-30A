#Q1.
numbersRepeat = [789,2,2,4,4,4,3,3,3,1]
#a. Sort and print.
numbersRepeat.sort()
print(numbersRepeat)
#b. Print the length.
print(len(numbersRepeat))
#c. Create a set out of our list.
numbersRepeat_set=set(numbersRepeat)
#d. Printing the set in sorted order.
#   We print it out as a list using sorted.
print(sorted(numbersRepeat_set))
#e. Adding 2 numbers to our set.
numbersRepeat_set.add(8128)
numbersRepeat_set.add(33550336)
print(numbersRepeat_set)
#f. Printing in sorted order using sorted().
print(sorted(numbersRepeat_set))
#g. Checking if 747 is in our set
print(747 in numbersRepeat_set)
#h. Using pop() to remove an item.
numbersRepeat_set.pop()
print(numbersRepeat_set)
#i. Printing the set in sorted order.
print(sorted(numbersRepeat_set))
#-------------------------------------------
#Q2.
presidents ={'Washington': 1, 'Lincoln': 16,
             'Kennedy': 35, 'Obama': 44}
#a. Adding a president.
presidents['Reagan']=40
#b. Printing our presidents.
for president in presidents:
    print(f"President: {president}")
#c. Checking if Nixon is present.
print('Nixon' in presidents)
#d. Using get() to find the location of Lincoln.
print(presidents.get('Lincoln'))
#e. Using del to delete Washington and printing dict.
#   We want to print in sorted order, so we use sorted.
del presidents['Washington']
print(sorted(presidents))
#f. Using get() to see if Obama is in our dict.
#   If he isn't, we output that he isn't in our dict.5
print(presidents.get('Obama',"Obama isn't in our dictionary."))
