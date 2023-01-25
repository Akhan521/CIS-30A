#Q1: Inches to centimeters.
print()
def inch_to_cent(inches):
    cent=inches*2.54
    print(f"{inches} inches = {cent} centimeters.")
#Converting 100 inches to centimeters.
inch_to_cent(100)
#-------------------------------------------------------------------------------
#Q2: Adding 2 numbers.
import sys
print()
print("Enter the first integer: ")
num1=int(sys.stdin.readline())
print("Enter the second integer: ")
num2=int(sys.stdin.readline())
#Our function to add 2 numbers:
def add_2(num1,num2):
    sum=num1+num2
    print(f"{num1} + {num2} = {sum}")
#Adding our 2 numbers:
add_2(num1,num2)
