import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x400')

root.title("Calculator")
root.iconbitmap('jose.ico')


def setTextInInputField(text):
    expression_field.delete(0, "end")
    expression_field.insert(0, text)


expression_field = tk.Entry(root, width=60)

plus_button = tk.Button(root, text='+', height=2, width=10, command=lambda: setTextInInputField("+"))
minus_button = tk.Button(root, text='-', height=2, width=10, command=lambda: setTextInInputField("-"))
multiply_button = tk.Button(root, text='*', height=2, width=10, command=lambda: setTextInInputField("*"))
divide_button = tk.Button(root, text='÷', height=2, width=10, command=lambda: setTextInInputField("÷"))
equals_button = tk.Button(root, text='=', height=2, width=10)

button1 = tk.Button(root, text="1", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("1"))
button2 = tk.Button(root, text="2", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("2"))
button3 = tk.Button(root, text="3", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("3"))
button4 = tk.Button(root, text="4", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("4"))
button5 = tk.Button(root, text="5", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("5"))
button6 = tk.Button(root, text="6", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("6"))
button7 = tk.Button(root, text="7", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("7"))
button8 = tk.Button(root, text="8", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("8"))
button9 = tk.Button(root, text="9", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("9"))
button0 = tk.Button(root, text="0", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField("10"))
buttonC = tk.Button(root, text="C", height=2, width=10, bg='green', fg='white', command=lambda: setTextInInputField(""))

expression_field.grid(row=1, column=1, columnspan=5)

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
