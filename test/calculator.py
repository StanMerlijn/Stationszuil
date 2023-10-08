from tkinter import *

root = Tk()
root.title("calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10,)


def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "add"
    f_num = float(first_number)
    entry.delete(0, END)


def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(first_number)
    entry.delete(0, END)


def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    entry.delete(0, END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    entry.delete(0, END)


def button_comma():
    current = entry.get()
    entry.delete(0, END)
    current = str(current) + "."
    float(current)
    entry.insert(0, current)


def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "add":
        entry.insert(0, f_num + float(second_number))
    if math == "subtract":
        entry.insert(0, f_num - float(second_number))
    if math == "multiply":
        entry.insert(0, f_num * float(second_number))
    if math == "divide":
        entry.insert(0, f_num / float(second_number))


def button_clear():
    entry.delete(0, END)


def button_click(number):
    # entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


button_bw = 2

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), borderwidth=button_bw)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), borderwidth=button_bw)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), borderwidth=button_bw)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), borderwidth=button_bw)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), borderwidth=button_bw)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), borderwidth=button_bw)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), borderwidth=button_bw)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), borderwidth=button_bw)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), borderwidth=button_bw)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), borderwidth=button_bw)
button_add = Button(root, text="+", padx=39, pady=20, command=button_add, borderwidth=button_bw)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal, borderwidth=button_bw)
button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clear, borderwidth=button_bw)

button_sub = Button(root, text="-", padx=41, pady=20, command=button_subtract, borderwidth=button_bw)
button_mult = Button(root, text="*", padx=40, pady=20, command=button_multiply, borderwidth=button_bw)
button_divide = Button(root, text="/", padx=42, pady=20, command=button_divide, borderwidth=button_bw)
button_comma = Button(root, text=".", padx=42, pady=20, command=button_comma, borderwidth=button_bw)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=6, column=1, columnspan=2)

button_mult.grid(row=4, column=2)
button_sub.grid(row=6, column=0)
button_divide.grid(row=4, column=1)
button_comma.grid(row=7, column=1)

root.mainloop()
