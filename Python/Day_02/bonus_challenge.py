#Create a Simple Calculator.
#Ask for:

#First Number:

#Second Number:

#Display:

#Addition
#Subtraction
#Multiplication
#Division
#Remainder
#Power

#Example:

#20 + 10 = 30
#20 - 10 = 10
#20 * 10 = 200
#20 / 10 = 2.0
#20 % 10 = 0
#20 ** 10 = 10240000000000

# Ask the user for two numbers and store them in variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
remainder = num1 % num2
power = num1 ** num2

# Display the results
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {remainder}")
print(f"{num1} ** {num2} = {power}")