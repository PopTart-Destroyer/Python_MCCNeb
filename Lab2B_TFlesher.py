# T.J. Flesher
# Info 2900
# P. Phillips
# Lab 2B

#Simple login program

#variables and constants
loginName = "GLucas001"
password = "THX1138"

#get user input
nameEntered = input("Enter your name: ")
passwordEntered = input("Enter your password: ")

#check user input against constants
if nameEntered == loginName and passwordEntered == password:
    print("Login successful!")
else:
    print("Login failed")
