from os import system, name
import math


# clears console
def clr():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


operators = ["+", "-", "*", "/", "root", "cos"]


def calculate(num1=None, num2=None, op=None):
    if op == 1:
        return num1 + num2
    if op == 2:
        return num1 - num2
    if op == 3:
        return num1 * num2
    if op == 4:
        return num1 / num2
    if op == 5:
        return math.sqrt(num1)
    if op == 6:
        return math.cos(num1)


# prints all available operators
def print_operators():
    for i in operators:
        print(str(operators.index(i) + 1) + ": " + i)


is_running = True
clr()
# get user operator choice
while is_running is True:
    print_operators()
    valid = False
    while valid is False:
        try:
            op = int(input("Select operator (1 - 6): "))
            if op in range(1, 7):
                valid = True
                clr()
        except ValueError:
            print("Enter a number between 1 - 6: ")

    # get first number
    x = False
    while x is False:
        try:
            num1 = int(input("Enter first number: "))
            x = True
        except ValueError:
            print("Enter a valid number: ")

    # get second number
    num2 = None
    if op != 5 and op != 6:
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result: " + str(calculate(num1, num2, op)))
    else:
        print("Result: " + str(calculate(num1, num2, op)))

    choice = str(input("Continue? (Y / N): "))
    if choice.lower() == "y":
        is_running = True
    elif choice.lower() == "n":
        is_running = False
