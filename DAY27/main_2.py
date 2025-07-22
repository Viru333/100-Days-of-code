from tkinter import *

window = Tk()
window.title("My First Label")
window.minsize(width=600, height=600)
# window.config(padx=100, pady=200)
my_label = Label(text="My label", font=("Times New Roman", 20, "italic"))
# my_label.place(x=200,y=0)
my_label.grid(column=0, row=0)
my_label["text"] = "Label is changed"
# my_label.config(text="New Text")
my_label.config(padx=50, pady=50)


def button_clicked():
    pass
    # new_text = entry.get()
    # my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

entry = Entry(width=10)
entry.grid(column=3, row=2)

















window.mainloop()
