#Q1: Printing numbers w/ a for loop:
print("Question 1:")
for num in range(2,18,2):
    print(num)
print()
#-------------------------------------------------------------------------------
#Q2: Dictionary problem:
print("Question 2:")
auto_items={'BMW':10,'Toyota':40,'Kia':30,'Ford':15}
#A list of preowned cars.
preowned_cars=['Toyota','Ford','Hyundai','Jeep','Chevy']
#How many preowned cars we have.
total=0
#Counting how many preowned cars we have in our dict.
for object,count in auto_items.items():
    if(object in preowned_cars):
        total+=count
print(f"We have {total} pre-owned cars.")
print()
#-------------------------------------------------------------------------------
#Q3: Using a nested for loop:
print("Question 3:")
nums=['One','Two','Three']
for i in nums:
    print(i)
    for j in nums:
        print(j)
    print()
print()
