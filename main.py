from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=50)
window.config(padx=10, pady=10)

isequal = Label(text="is equal to", font=("Calibri", 10))
isequal.grid(column=1, row=1)

zero = Label(text="0", font=("Calibri", 10))
zero.grid(column=2, row=1)

miles = Label(text="Miles", font=("Calibri", 10))
miles.grid(column=3, row=0)

km = Label(text="Km", font=("Calibri", 10))
km.grid(column=3, row=1)

input = Entry(width=10)
input.grid(column=2, row=0)


def calculating(*args):
    miles = float(input.get())
    km = round(miles * 1.60934)
    zero.config(text=km)


calculate = Button(text="Calculate", command=calculating)
calculate.grid(column=2, row=2)
calculate.config(padx=5, pady=1)


window.mainloop()
