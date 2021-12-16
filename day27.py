from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(text="new text")

# Button


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
input.get()




window.mainloop()
