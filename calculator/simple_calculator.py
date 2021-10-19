from tkinter import *

is_result = False
string = " "
root = Tk()
root.title("simple calculator")
photo = PhotoImage(file="calculator.png")
root.iconphoto(True, photo)
root.geometry("301x313")
root.resizable(0, 0)
input_field = Entry(root, borderwidth=5, width=45, justify=RIGHT)
input_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def calcutation(string1: str):
    global string
    global is_result
    temp = is_result
    if temp:
        input_field.delete(0, END)
        is_result = False

    input_field.insert(END, string1)
    string += string1


def clear_scrn():
    input_field.delete(0, END)


def result():
    global is_result
    is_result = True
    global string
    temp = eval(string)
    input_field.delete(0, END)
    input_field.insert(0, temp)
    string = " "


button_1 = Button(root, text="1", padx=40, pady=10, command=lambda: calcutation("1")).grid(row=1, column=0)
button_2 = Button(root, text="2", padx=40, pady=10, command=lambda: calcutation("2")).grid(row=1, column=1)
button_3 = Button(root, text="3", padx=40, pady=10, command=lambda: calcutation("3")).grid(row=1, column=2)
button_4 = Button(root, text="4", padx=40, pady=10, command=lambda: calcutation("4")).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=10, command=lambda: calcutation("5")).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=10, command=lambda: calcutation("6")).grid(row=2, column=2)
button_7 = Button(root, text="7", padx=40, pady=10, command=lambda: calcutation("7")).grid(row=3, column=0)
button_8 = Button(root, text="8", padx=40, pady=10, command=lambda: calcutation("8")).grid(row=3, column=1)
button_9 = Button(root, text="9", padx=40, pady=10, command=lambda: calcutation("9")).grid(row=3, column=2)
button_0 = Button(root, text="0", padx=40, pady=10, command=lambda: calcutation("0")).grid(row=4, column=0)
button_sum = Button(root, text="+", padx=39, pady=10, command=lambda: calcutation("+")).grid(row=4, column=1)
button_sub = Button(root, text="-", padx=41, pady=10, command=lambda: calcutation("-")).grid(row=4, column=2)
button_clear = Button(root, text="CE", padx=36, pady=10, command=clear_scrn).grid(row=5, column=0)
button_div = Button(root, text="/", padx=41, pady=10, command=lambda: calcutation("/")).grid(row=5, column=1)
button_mul = Button(root, text="*", padx=41, pady=10, command=lambda: calcutation("*")).grid(row=5, column=2)
button_equal = Button(root, text="=", padx=140, pady=10, command=result).grid(row=6, column=0, columnspan=3)
root.mainloop()
