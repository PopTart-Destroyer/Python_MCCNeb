# T.J. Flesher
# Info 2900
# P. Phillips
# Lab2A - Try Looping

# Fahrenheit to Celsius or Celsius to Fahrenheit Converter

#display instructions
print("Enter 'C' to convert a Celsius temperature to Fahrenheit")
print("or")
print("Enter 'F' to convert a Fahrenheit temperature to Celsius")

#get user input
cF = input(":")

while cF.upper() == "C" or cF.upper() == "F":
    temperature = float(input("Enter a temperature: "))
    if cF.upper() == "C":
        cToF = (temperature * 9/5) + 32
        print(temperature, "degrees Celsius is", cToF, "degrees Fahrenheit\n")
    elif cF.upper() == "F":
        fToC = (temperature - 32) * 9/5
        print(temperature, "degrees Fahrenheit is", fToC, "degrees Celsius\n")

    print("Enter 'C' to convert a Celsius temperature to Fahrenheit")
    print("or")
    print("Enter 'F' to convert a Fahrenheit temperature to Celsius")

    #get user input
    cF = input(":")

print("Start over -- and please select a 'C' or 'F' from the menu.")
