from tkinter import *


def comm_add():
    if not('+' in sign_box.get("1.0", END)):
        sign_box.delete("1.0", END)
        sign_box.insert(END, '+')


def comm_sub():
    if not('-' in sign_box.get("1.0", END)):
        sign_box.delete("1.0", END)
        sign_box.insert(END, '-')


def comm_div():
    if not('/' in sign_box.get("1.0", END)):
        sign_box.delete("1.0", END)
        sign_box.insert(END, '/')


def comm_mul():
    if not('*' in sign_box.get("1.0", END)):
        sign_box.delete("1.0", END)
        sign_box.insert(END, '*')


#def comm_result():
#    if not('=' in sign_box.get("1.0", END) or len(display_box.get("1.0", END)) < 1):
#        display_box.insert(END, '-')


def comm_1():
    display_box.insert(END, '1')


def comm_2():
    display_box.insert(END, '2')


def comm_3():
    display_box.insert(END, '3')


def comm_4():
    display_box.insert(END, '4')


def comm_5():
    display_box.insert(END, '5')


def comm_6():
    display_box.insert(END, '6')


def comm_7():
    display_box.insert(END, '7')


def comm_8():
    display_box.insert(END, '8')


def comm_9():
    display_box.insert(END, '9')


def comm_0():
    display_box.insert(END, '0')


def comm_ac():
    display_box.delete("1.0", END)
    sign_box.delete("1.0", END)


memory = 0              ##serves as a number memory that was put in the calculator


window = Tk()
window.title("Calculator")


sign_box = Text(window, height=2, width=4)
sign_box.grid(row=0, column=0)
sign_box.delete("1.0", END)

display_box = Text(window, height=2, width=10)
display_box.grid(row=0, column=4)
display_box.delete("1.0", END)


button_ac = Button(window, text='AC', height=2, width=4, command=comm_ac)
button_ac.grid(row=1, column=0)

button_add = Button(window, text='+', height=2, width=4, command=comm_add)
button_add.grid(row=2, column=4)

button_sub = Button(window, text='-', height=2, width=4, command=comm_sub)
button_sub.grid(row=3, column=4)

button_div = Button(window, text='/', height=2, width=4, command=comm_div)
button_div.grid(row=4, column=4)

button_mul = Button(window, text='*', height=2, width=4, command=comm_mul)
button_mul.grid(row=5, column=4)

button_result = Button(window, text='=', height=2, width=4)
button_result.grid(row=1, column=4)

button_0 = Button(window, text='0', height=2, width=4, command=comm_0)
button_0.grid(row=5, column=1)

button_1 = Button(window, text='1', height=2, width=4, command=comm_1)
button_1.grid(row=4, column=0)

button_2 = Button(window, text='2', height=2, width=4, command=comm_2)
button_2.grid(row=4, column=1)

button_3 = Button(window, text='3', height=2, width=4, command=comm_3)
button_3.grid(row=4, column=2)

button_4 = Button(window, text='4', height=2, width=4, command=comm_4)
button_4.grid(row=3, column=0)

button_5 = Button(window, text='5', height=2, width=4, command=comm_5)
button_5.grid(row=3, column=1)

button_6 = Button(window, text='6', height=2, width=4, command=comm_6)
button_6.grid(row=3, column=2)

button_7 = Button(window, text='7', height=2, width=4, command=comm_7)
button_7.grid(row=2, column=0)

button_8 = Button(window, text='8', height=2, width=4, command=comm_8)
button_8.grid(row=2, column=1)

button_9 = Button(window, text='9', height=2, width=4, command=comm_9)
button_9.grid(row=2, column=2)


window = mainloop()
