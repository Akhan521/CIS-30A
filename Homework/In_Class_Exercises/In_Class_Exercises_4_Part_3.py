#Q1: Printing numbers using an f-string.
for i in range(1,4):
    print(i)
    for j in range(1,4):
        print(f"{i*2}")
print()
for i in range(1,4):
    j=i*2
    print(f"{i} {j}")
#-------------------------------------------------------------------------------
#Q2: Defining a function to determine if we have an odd number.
print()
def isOdd(num):
    return num%2==1
#Driver code.
num=int(input("Enter an integer: "))
print("ODD" if isOdd(num) else "EVEN")
