from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="new text")
my_label.config(padx=20, pady=30)
# Button


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=2)

button1 = Button(text="Click1 me", command=button_clicked)
button1.grid(column=3, row=0)

# Entry
input = Entry(width=10)
input.grid(column=6, row=4)
input.get()




window.mainloop()
