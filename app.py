from tkinter import *

global sign
sign = ' '
global current_num
current_num = ' '


def button_equal():
    global current_num
    global sign
    if current_num != ' ' and sign != ' ':
        second_num = display_box.get("1.0", END)
        display_box.delete("1.0", END)
        if sign == "+":
            display_box.insert(END, float(current_num) + float(second_num))
        elif sign == "-":
            display_box.insert(END, float(current_num) - float(second_num))
        elif sign == "/" and second_num != "0":
            display_box.insert(END, float(current_num) / float(second_num))
        else:
            display_box.insert(END, float(current_num) * float(second_num))
        current_num = " "
        sign = " "
        button_div.configure(bg="white")
        button_mul.configure(bg="white")
        button_sub.configure(bg="white")
        button_add.configure(bg="white")


def button_add():
    global sign
    global current_num
    if sign == "+":
        if current_num != " ":
            # second_num = display_box.get("1.0", END)
            # display_box.delete("1.0", END)
            # display_box.insert(END, float(current_num) + float(second_num))
            button_equal
        else:
            sign = " "
            button_add.configure(bg="white")

    else:
        sign = "+"
        button_div.configure(bg="white")
        button_mul.configure(bg="white")
        button_sub.configure(bg="white")
        button_add.configure(bg="blue")


def button_subtract():
    global sign
    if sign == "-":
        sign = " "
        button_sub.configure(bg="white")
    else:
        sign = "-"
        button_add.configure(bg="white")
        button_div.configure(bg="white")
        button_mul.configure(bg="white")
        button_sub.configure(bg="blue")


def button_divide():
    global sign
    if sign == "/":
        sign = " "
        button_div.configure(bg="white")
    else:
        sign = "/"
        button_add.configure(bg="white")
        button_mul.configure(bg="white")
        button_sub.configure(bg="white")
        button_div.configure(bg="blue")


def button_multiply():
    global sign
    if sign == "*":
        sign = " "
        button_mul.configure(bg="white")
    else:
        sign = "*"
        button_div.configure(bg="white")
        button_add.configure(bg="white")
        button_sub.configure(bg="white")
        button_mul.configure(bg="blue")


def button_click(number):
    global sign
    global current_num
    if sign != ' ':
        current_num = display_box.get("1.0", END)
        display_box.delete("1.0", END)
    display_box.insert(END, number)


def button_point():
    if '.' not in display_box.get("1.0", END) and len(display_box.get("1.0", END)) > 1:
        display_box.insert(END, '.')


def comm_ac():
    display_box.delete("1.0", END)


window = Tk()
window.title("Calculator")
window.iconbitmap("calc.ico")


# 0 row initialisation
display_box = Text(window, height=3, width=25)
display_box.delete("1.0", END)
button_equal = Button(window, text='=', padx=25, pady=20, command=button_equal, bd=6)
# 1 row buttons initialisation
button_7 = Button(window, text='7', padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text='8', padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text='9', padx=30, pady=20, command=lambda: button_click(9))
button_add = Button(window, text='+', padx=25, pady=20, command=button_add, bd=6)
# 2 row buttons initialisation
button_4 = Button(window, text='4', padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text='5', padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text='6', padx=30, pady=20, command=lambda: button_click(6))
button_sub = Button(window, text='-', padx=25, pady=20, command=button_subtract, bd=6)
# 3 row buttons initialisation
button_1 = Button(window, text='1', padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text='2', padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text='3', padx=30, pady=20, command=lambda: button_click(3))
button_div = Button(window, text='/', padx=25, pady=20, command=button_divide, bd=6)
# 4 row buttons initialisation
button_ac = Button(window, text='AC', padx=26, pady=20, command=comm_ac)
button_0 = Button(window, text='0', padx=30, pady=20, command=lambda: button_click(0))
button_point = Button(window, text='.', padx=30, pady=20, command=button_point)
button_mul = Button(window, text='*', padx=25, pady=20, command=button_multiply, bd=6)

# 0 row localisation
display_box.grid(row=0, column=0, columnspan=3)
button_equal.grid(row=0, column=4)
# 1 row buttons localisation
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=4)
# 2 row buttons localisation
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=4)
# 3 row buttons localisation
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=4)
# 4 row buttons localisation
button_ac.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_point.grid(row=4, column=2)
button_mul.grid(row=4, column=4)

window = mainloop()
