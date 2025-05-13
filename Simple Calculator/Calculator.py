# Simple Calculator - Python Programming

# Prompting the user for inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation:")
print(" + for addition")
print(" - for subtraction")
print(" * for multiplication")
print(" / for division")
print(" % for remainder")
operation = input("Enter your choice (+, -, *, /, %):")

# Performing the arithmetic operation and displaying the result
if operation == '+':
    result = num1 + num2
    print("Result:", result)

elif operation == '-':
    result = num1 - num2
    print("Result:", result)

elif operation == '*':
    result = num1 * num2
    print("Result:", result)

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
        
elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print("Result (Remainder):", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
