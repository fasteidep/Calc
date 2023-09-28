import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or  '-' in value or '*' in value or'/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)

def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Error', 'Можно вводить только цифры и математические знаки (+-/*)')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Error', 'На ноль делить нельзя')
        calc.insert(0, 0)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)

def make_digit_button(digit):
    return tk.Button(text=digit, bd=0, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=0, font=('Arial', 13), fg='red',
                     command=lambda: add_operation(operation))

def make_cal_button(operation):
    return tk.Button(text=operation, bd=0, font=('Arial', 13), fg='red',
                     command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=0, font=('Arial', 13), fg='red',
                     command=clear)

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

h = 240
w = 270

# Информация про окно
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
icon = tk.PhotoImage(file='calculator.png')
window.iconphoto(False, icon)
window.geometry(f"{h}x{w}")
window['bg'] = '#33ffe6'

window.bind('<Key>', press_key)

calc = tk.Entry(window, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)
make_digit_button('1').grid(row=1, column=0, sticky='nwes', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, sticky='nwes', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, sticky='nwes', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, sticky='nwes', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, sticky='nwes', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, sticky='nwes', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, sticky='nwes', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, sticky='nwes', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, sticky='nwes', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, sticky='nwes', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, sticky='nwes', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='nwes', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, sticky='nwes', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, sticky='nwes', padx=5, pady=5)

make_cal_button('=').grid(row=4, column=2, sticky='nwes', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, sticky='nwes', padx=5, pady=5)



window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)

window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)
window.grid_rowconfigure(3, minsize=60)
window.grid_rowconfigure(4, minsize=60)

window.mainloop()
