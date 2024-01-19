print("This is a simple calculator. Enter two numbers and an operator.")

num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))

operator: str = input("Enter an operator (+, -, *, /). ")

plus: str = "+"
minus: str = "-"
multiplier: str = "*"
divisor: str = "/"

if operator == plus:
    print("Result: ", num1 + num2)
elif operator == minus:
    print("Result: ", num1 - num2)
elif operator == multiplier:
    print("Result: ", num1 * num2)
elif operator == divisor:
    print("Result:", num1 / num2 if num2 != 0 else "You can’t divide it by zero!")
else:
    print("You entered the wrong operator.")
