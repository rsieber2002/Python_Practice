#This file is just to practice some basic computations utilizing prompts and variables

#Get variables
var1 = float(input("Please enter a number: "))
var2 = float(input("Please enter a second number: "))

operation = input("Please enter one of the following: +, -, /, or *: ")

if operation == "+":
    result = var1 + var2
elif operation == "-":
    result = var1 - var2
elif operation == "/":
    result = var1 / var2
elif operation == "*":
    result = var1 * var2
else:
    print("You have entered an invalid operation!")
    exit()

print("The result is " + str(result))