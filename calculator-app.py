def calculate(num1, num2, operation):

# mathmatical operation with two number#
# args: num1: first number, num2: second number, operation: +, -, *, /
# returns: result of operation OR None if invalid

    if operation == '+':
        return num1 + num2

    elif operation == '-':
        return num1 - num2

    elif operation == '*':
        return num1 * num2

    elif operation == '/':
        if num2 != 0: 
            return num1 / num2
        else:
            print("Error: Division by zero not allowed.")  
            return None

    else: 
        print("Error: Invalaid operation.")
        return None

#user input
try: 
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operation = input("Enter operation symbol (+. -, *, /: )")

    result = calculate(number1, number2, operation)

    if result is not None:
        print(f"Result equalls: {result}")

except ValueError: 
        print("Invalid input. Enter valid numbers.")