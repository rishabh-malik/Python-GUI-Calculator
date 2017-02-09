from tkinter import *
import parser

root = Tk()
root.title('Calculator')

i = 0


def factorial():
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number
    try:
        while counter > 0:
            fact = fact * counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def clear_all():
    display.delete(0, END)


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def undo():
    whole_string = display.get()
    if len(whole_string):
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error, press AC")


def calculate():
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")


root.columnconfigure(0)
root.columnconfigure(1)
root.columnconfigure(2)
root.columnconfigure(3)
root.columnconfigure(4)

root.rowconfigure(0)
root.rowconfigure(1)
root.rowconfigure(2)
root.rowconfigure(3)


display = Entry(root, font=("Calibri", 13))
display.grid(row=1, columnspan=6, sticky=W + E)

one = Button(root, text="1", command=lambda: get_variables(1))
one.grid(row=2, column=0)
two = Button(root, text="2", command=lambda: get_variables(2))
two.grid(row=2, column=1)
three = Button(root, text="3", command=lambda: get_variables(3))
three.grid(row=2, column=2)

four = Button(root, text="4", command=lambda: get_variables(4))
four.grid(row=3, column=0)
five = Button(root, text="5", command=lambda: get_variables(5))
five.grid(row=3, column=1)
six = Button(root, text="6", command=lambda: get_variables(6))
six.grid(row=3, column=2)

seven = Button(root, text="7", command=lambda: get_variables(7))
seven.grid(row=4, column=0)
eight = Button(root, text="8", command=lambda: get_variables(8))
eight.grid(row=4, column=1)
nine = Button(root, text="9", command=lambda: get_variables(9))
nine.grid(row=4, column=2)

cls = Button(root, text="AC", command=clear_all, foreground="red")
cls.grid(row=5, column=0)
zero = Button(root, text="0", command=lambda: get_variables(0))
zero.grid(row=5, column=1)
result = Button(root, text="=", command=calculate, foreground="red")
result.grid(row=5, column=2)

plus = Button(root, text="+", command=lambda: get_operation("+"))
plus.grid(row=2, column=3)
minus = Button(root, text="-", command=lambda: get_operation("-"))
minus.grid(row=3, column=3)
multiply = Button(root, text="*", command=lambda: get_operation("*"))
multiply.grid(row=4, column=3)
divide = Button(root, text="/", command=lambda: get_operation("/"))
divide.grid(row=5, column=3)


root.mainloop()
