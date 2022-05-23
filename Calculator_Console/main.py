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


operators = ["+", "-", "*", "/", "root", "square"]


def calculate(number1=None, number2=None, operator=None):
    match operator:
        case 1:
            return number1 + number2
        case 2:
            return number1 - number2
        case 3:
            return number1 * number2
        case 4:
            return number1 / number2
        case 5:
            return math.sqrt(number1)
        case 6:
            return math.sqrt(number1)
        case _:
            return 0


# prints all available operators
def print_operators():
    for i in operators:
        print(str(operators.index(i) + 1) + ": " + i)


is_running = True
clr()
# get user operator choice
while is_running is True:
    print_operators()
    opIsValid = False
    while opIsValid is False:
        try:
            op = int(input("Select operator (1 - 6): "))
            if op in range(1, 7):
                opIsValid = True
                clr()
        except ValueError:
            print("Enter a number between 1 - 6: ")

    # get first number
    num1IsValid = False
    while num1IsValid is False:
        try:
            num1 = int(input("Enter first number: "))
            if op != 5 and num1 < 0:
                print("Can't take the root of a negative number!")
            else:
                num1IsValid = True

        except ValueError:
            print("Enter a valid number: ")

    # get second number
    num2IsValid = False
    num2 = None
    if op != 5 and op != 6:
        while num2IsValid is False:
            try:
                num2 = int(input("Enter second number: "))
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print("Result: " + str(calculate(num1, num2, op)))
                    num2IsValid = True
            except ValueError:
                print("Enter a valid number: ")
    else:
        print("Result: " + str(calculate(num1, num2, op)))

    choice = ""
    while choice.lower() != "y" and choice.lower() != "n":
        choice = str(input("Continue? (Y / N): "))
        if choice.lower() == "y":
            is_running = True
        elif choice.lower() == "n":
            is_running = False
