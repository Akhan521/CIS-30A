#Q1: Printing whether an integer is + or -.
print()
num=int(input("Enter an integer: "))
if num>0:
    print(num,"is a positive integer.")
else:
    print(num,"is NOT a positive integer.")
print()
print("This is always printed.")
#-------------------------------------------------------------------------------
#Q2: Checking to see if we have a perfect number.
print()
pnum=int(input("Enter a positive integer: "))
#If we have a positive integer, we check to see if it's perfect.
if(pnum>0):
    if(pnum==6):
        print("That's a perfect number!")
    elif(pnum==28):
        print("That's a perfect number!")
    elif(pnum==496):
        print("That's a perfect number!")
    elif(pnum==8128):
        print("That's a perfect number!")
    elif(pnum==33550336):
        print("That's a perfect number!")
    else:
        print("That is NOT a perfect number!")
#Otherwise, we print a message saying a negative integer was entered.
else:
    print("You did not enter a positive integer.")
print()
print("This is always printed.")
