import tkinter as tk

root = tk.Tk()
root.geometry('400x400')

root.title("Calculator")
root.iconbitmap('jose.ico')

numberInTextField = ""
operator = ""
number1 = 0
number2 = 0
firstNumber1 = True
result = ""


def setTextInInputField(text):
    expression_field.delete(0, "end")
    expression_field.insert(0, text)


def updateExpression(number):
    global numberInTextField
    numberInTextField = numberInTextField + str(number)
    setTextInInputField(numberInTextField)


def resetExpression():
    global numberInTextField
    numberInTextField = ""
    numberInTextField = numberInTextField


def chooseOperator(chosenOperator):
    global operator, firstNumber1
    operator = chosenOperator
    setTextInInputField(chosenOperator)
    firstNumber1 = False

def setNumber():

    global number1, number2
    if firstNumber1:
        number1 = int(numberInTextField)

    else:
        number2 = int(numberInTextField)


def calculation():
    global result
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2

    setTextInInputField(result)


expression_field = tk.Entry(root, width=60)

button1 = tk.Button(root, text=1, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button1.cget('text')),
                                     setNumber()])
button2 = tk.Button(root, text=2, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button2.cget('text')),
                                     setNumber()])
button3 = tk.Button(root, text=3, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button3.cget('text')),
                                     setNumber()])
button4 = tk.Button(root, text=4, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button4.cget('text')),
                                     setNumber()])
button5 = tk.Button(root, text=5, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button5.cget('text')),
                                     setNumber()])
button6 = tk.Button(root, text=6, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button6.cget('text')),
                                     setNumber()])
button7 = tk.Button(root, text=7, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button7.cget('text')),
                                     setNumber()])
button8 = tk.Button(root, text=8, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button8.cget('text')),
                                     setNumber()])
button9 = tk.Button(root, text=9, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button9.cget('text')),
                                     setNumber()])
button0 = tk.Button(root, text=0, height=2, width=10, bg='green', fg='white',
                    command=lambda: [updateExpression(button0.cget('text')),
                                     setNumber()])
buttonC = tk.Button(root, text="C", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField(""))

expression_field.grid(row=1, column=1, columnspan=5)

plus_button = tk.Button(root, text='+', height=2, width=10,
                        command=lambda: [chooseOperator(plus_button.cget('text')), resetExpression()])
minus_button = tk.Button(root, text='-', height=2, width=10,
                         command=lambda: [chooseOperator(minus_button.cget('text')), resetExpression()])
multiply_button = tk.Button(root, text='*', height=2, width=10,
                            command=lambda: [chooseOperator(multiply_button.cget('text')), resetExpression()])
divide_button = tk.Button(root, text='÷', height=2, width=10,
                          command=lambda: [chooseOperator(divide_button.cget('text')), resetExpression()])
equals_button = tk.Button(root, text='=', height=2, width=10, command=lambda: calculation())

plus_button.grid(row=2, column=4)
minus_button.grid(row=3, column=4)
multiply_button.grid(row=4, column=4)
divide_button.grid(row=5, column=4)
equals_button.grid(row=5, column=3)

button1.grid(row=2, column=1)
button2.grid(row=2, column=2)
button3.grid(row=2, column=3)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
button7.grid(row=4, column=1)
button8.grid(row=4, column=2)
button9.grid(row=4, column=3)
button0.grid(row=5, column=1)
buttonC.grid(row=5, column=2)

root.mainloop()
