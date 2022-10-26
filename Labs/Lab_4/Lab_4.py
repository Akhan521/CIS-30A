#Q1: Using an if-else statement.
print()
age=int(input("Enter your age as an integer: "))
if age >= 21:
    print("You've met the legal drinking age.")
else:
    print("You are a minor. You can't drink.")
#-------------------------------------------------------------------------------
#Q2: Checking for a name in a list.
print()
banned_users=['Andrew','Carole','David']
user="Marie"
if(user not in banned_users):
    print(f"{user}, you can post a response if you wish.")
else:
    print(f"{user}, you are banned from making a response.")
#-------------------------------------------------------------------------------
#Q3: Adding odd numbers.
print()
#Our numbers.
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10,
            17,312, 542, 87, 23, 86, 191, 116, 35,
            173, 45,149, 59, 84, 69, 113, 166]
#Our sum.
sum=0
#The number of odd numbers we've added.
oddNums=0
#Finding 5 odd numbers to add.
for i in range(len(num_list)):
    #If we have an odd number...
    if(num_list[i]%2==1):
        sum+=num_list[i] #We add it.
        oddNums+=1       #We increment our count by 1.
    #If we've added 5 odd numbers, we exit.
    if(oddNums==5):
        break
#Printing our sum.
print(f"The sum of the first 5 odd numbers is: {sum:d}")
#-------------------------------------------------------------------------------
#Q4: Creating a 140 character news ticker with different headlines.
print()
#Our headlines list.
headlines=[
 'White House urges borrowers to apply for student debt relief despite court order',
 'Las Vegas teen dies from brain-eating amoeba as experts warn against panic',
 'White House denies talk of national security review of Elon Musk ventures'
 ]
#Our news ticker.
news_ticker=""
#We loop over every headline in our list.
for headline in headlines:
    #We loop over every character in each headline.
    for character in headline:
        #We add it to our news ticker.
        news_ticker=news_ticker+character
        #If it's 140 characters, we break our of our 2nd loop.
        if(len(news_ticker)==140):
            break
    #If it's 140 characters, we break out of our 1st loop.
    if(len(news_ticker)==140):
        break  
    #After every headline, we add a space.
    news_ticker=news_ticker+" "
#Printing our final news ticker.
print("Length of news_ticker: ",len(news_ticker))
print(news_ticker)
#-------------------------------------------------------------------------------
#Q5: Prime numbers.
print()
#A list of numbers that we'll check.
check_prime=[2,4,5,6,8,23,27,33,36]
#Checking every number in our list.
for num in check_prime:
    #To hold a factor if we have one.
    factor=-1
    #To store whether we have a prime number.
    isPrime=True
    #Checking whether we have another factor.
    for i in range(2,num):
        #If we have another factor besides 1 and the number itself...
        if (num%i==0):
            factor=i      #We store the factor.
            isPrime=False #We set it as a non-prime number.
            break
    if(isPrime):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number, and {factor} is a factor of {num}.")
#-------------------------------------------------------------------------------
#Q6: Population density function.
print()
def population_density(population,land_area):
    #Calculate the population density and return it.
    return population/land_area
#Test case 1:
test1=population_density(10,1)
expected_result1=10
print("Expected result: {}, Actual result: {:.0f}"
      .format(expected_result1,test1))
#Test case 2:
test2=population_density(864816,121.4)
expected_result2=7123.6902801
print("Expected result: {}, Actual result: {:.7f}"
      .format(expected_result2,test2))
#-------------------------------------------------------------------------------
#Q7: Readable time-delta.
print()
def readable_timedelta(days):
    weeks=int(days/7)
    days-=(weeks*7)
    return f"{weeks} week(s) and {days} day(s)."
print(readable_timedelta(10))
#-------------------------------------------------------------------------------
#Q8: Printing whether numbers in a range are divisible by 2.
print()
num=int(input("Enter an integer: "))
#We see which numbers from 1-num are divisble by 2.
for i in range(1,num+1):
    if(i%2==0):
        print(i," is divisible by 2.")
    else:
        print(i," is NOT divisible by 2.")
#-------------------------------------------------------------------------------
#Q9: Print vs. return.
print()
print("Print vs. Return:")
def show_plus_ten(num):
    print(num+10)
def add_ten(num):
    return num+10
show_plus_ten(5)  #Prints it.
print(add_ten(5)) #Returns it.
#-------------------------------------------------------------------------------
#Q10: Factorials.
print()
num=int(input("Enter a positive integer: "))
if(num<0):
    print("That is a negative number!")
else:
    #To hold the result.
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f"{num}! = {fact}")
#-------------------------------------------------------------------------------
#Q11: Gain weight function.
print()
def gain_weight(weight,increase):
    #Displaying information for 52 weeks.
    for i in range(1,53):
        #Printing our weight.
        print(f"Week {i}: {weight+increase} pounds.")
        #Adding to our weight.
        weight+=increase
#Calling our function.
gain_weight(140,0.5)
    
