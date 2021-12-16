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

km = Label(text="KM", font=("Calibri", 10))
km.grid(column=3, row=1)


def button_clicked():
    print("eheh")


calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=2, row=2)
calculate.config(padx=5, pady=1)

input = Entry(width=10)
input.grid(column=2, row=0)
input.get()



window.mainloop()
