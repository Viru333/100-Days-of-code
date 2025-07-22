from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("Widget Examples")

# Heading of the GUI
new_label = Label(text="This is new text", font=("Times New Roman", 14, "normal"))
new_label.pack()


def button_clicked():
    new_text = entry.get()
    new_label.config(text=new_text)


# A button to perform some actions
button = Button(text="Click me", command=button_clicked)
button.pack()
# Entries
entry = Entry(width=30)

# Add some text to begin with
entry.insert(END, string="some text to begin with.")

# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)

# Puts cursor in textbox
text.focus()

# Add some text to begin with

text.insert(END, "Example of a multi-line text entry.")

# Get's current value in textbox at line 1, character 0

print(text.get("1.0", END))
text.pack()

# Spinbox


def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    # Prints 1 if On Button Checked, otherwise 0.
    print(checked_state.get())

# Variable to hold on to checked state, 0 is Off, 1 is On.
checked_state = IntVar() # IntVar() is a class
checkbutton = Checkbutton(text="IsOn?",variable=checked_state, command=checkbutton_used)

checked_state.get()
checkbutton.pack()

# Radiobutton

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()

# Listbox

def listbox_used(event):
    # GEts current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()











window.mainloop()