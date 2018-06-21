# T.J. Flesher
# INFO 2900
# P. Phillips
# Lab3A

#Program 1 - Treadmill Calories

# Variables/constants

CONST_CPM = 4.2
temp = 0

for i in range(5):
    temp += CONST_CPM
    print(i+ 1, 'minute(s) burns', round(temp,1), "calories")


#Program 2 - Treadmill Calories 2

# Variables/constants

CONST_CPM = 4.2
temp = 0
for i in [10,15,20,25,30]:
    temp = CONST_CPM * i
    print(i, 'minute(s) burns', round(temp,1), "calories")
    
#Program 3 - Program Sprints (5 Days Weeks)

# Variables/constants

CONST_SPRINT = 5
numberOfProjects = 0.0

for i in range(CONST_SPRINT):
    numberOfProjects += float(input("Number of project finished on day {}:".format(i + 1)))

print("A total of", numberOfProjects,"projects were finished this week.")
print("That is", numberOfProjects / CONST_SPRINT,"projects per day.")

#Program 4 - Convert inches to centimeters

# Variables/constants

cToInches = 2.54

# Welcome display
print("Welcome to the inches to centimeters converters program!")

# Get user input/while loop
done = 'Y'
while done.upper() == 'Y':
    inches = float(input("Enter a number in inches:"))
    print("That is", round(cToInches * inches,3),"centimeters long.")
    done = input("If you wish to continue, enter a 'Y'.  Anthing else will end the program:")
    
print("\nGoodbye!")

#Program 5 - Convert inches to centimeters w/ user input being gt zero

# Variables/constants

cToInches = 2.54

# Welcome display
print("Welcome to the inches to centimeters converters program!")

# Get user input/while loop
done = 'Y'
while done.upper() == 'Y':
    inches = float(input("Enter a number of inches (greater than zero):"))
    while inches <= 0:
        inches = float(input("That is not a correct value. Enter a number of inches greater than zero:"))
        
    print("That is", round(cToInches * inches,3),"centimeters long.")
    done = input("If you wish to continue, enter a 'Y'.  Anthing else will end the program:")
    
print("\nGoodbye!")

