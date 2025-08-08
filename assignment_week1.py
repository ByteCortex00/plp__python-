'''
Instructions:

Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

'''

# Getting user input
var_1 = int(input("Enter the first number: "))
var_2 = int(input("Enter the second number: "))
operator = input("Enter the operator sign(*,-,+,/): ")

if operator == '+':
    addition = var_1 + var_2
    print(f'sum of {var_1} and {var_2} = {addition}')
elif operator == '*':
    multiplication = var_1 * var_2
    print(f'multiplication of {var_1} and {var_2} = {multiplication}')
elif operator == '-':
    subtraction = var_1 - var_2
    print(f' Subtraction of {var_1} and {var_2} = {subtraction}')
elif operator == "/":
    if var_2 != 0:
        division = var_1/var_2
        print(f' Division of {var_1} and {var_2} = {division}')

    else:
        print("Error: Division by zero")
else:
    print("Invalid operation select from +,-,* or /")
