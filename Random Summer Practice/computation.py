#This file is just to practice some basic computations utilizing prompts and variables

#Get variables
var1 = input("Please enter a number: ")
var2 = input("Please enter a second number: ")

operation = input("Please enter one of the following: +, -, /, or *")

if operation == "+":
    result = var1 + var2
else if operation == "-":
    result = var1 - var2
else if operation == "/":
    result = var1 / var2
else if operation == "*":
    result = var1 * var2
else:
    print("You have entered an invalid operation!")
    break

print("The result is " + result)