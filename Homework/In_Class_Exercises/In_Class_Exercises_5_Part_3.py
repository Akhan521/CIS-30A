#Q1 - Understanding different exceptions.
print()
print("Question 1:")
print("-----------")
#Supplied Code:
try:
    #Storing 2 integers.
    userInput1 = int(input("Please enter an integer: "))
    userInput2 = int(input("Please enter another integer: "))
    #Dividing them.
    answer = userInput1/userInput2
    #Displaying the result.
    print("The answer is", answer)
    #Opening a file. (Used to demonstrate an unknown error.)
    myFile = open("missing.txt", 'r')
#Value Error.
except ValueError:
    print("Error: You did not enter an integer.")
#Zero Division Error.
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
#A General Exception.
except Exception as e:
    print("Unknown Error: ", e)

# 1. Try typing the letter m. (Not an integer.)
# -> This results in a Value Error, so the 1st except block is executed.
# 2. Try 12 for the first number then 0 for the second number.
# -> This results in a Zero Division Error. (The 2nd block is executed.)
# 3. Try 12 for the first number then 3 for the second number.
# Then, explain why you have a unknown error at the end of the output.
# -> This results in an unknown error because we're trying to open a file
#    that does not exist. We get an error because the file can't be found.
#-------------------------------------------------------------------------------
#Q2 - Demonstrating a type error.
print()
print("Question 2:")
print("-----------")
#Our list of characters.
disney_list=['Mickey','Minnie','Donald','Daisy']
#Our list of indices.
indices=[0,1,"2",3]
#Looping through our indices list.
for i in indices:
    #We attempt to print a character using an index.
    try:
        print(disney_list[i])
    #Type Error.
    except TypeError:
        print("TypeError: Check your list of indices.")
