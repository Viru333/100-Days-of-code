from tkinter import *

window = Tk()
window.minsize(width=400, height=200)
window.title("Mile to Km Converter")

def Convert_to_km():
    n_miles = int(entry.get())
    x_km = 1.60934*n_miles
    output.config(text=f"{x_km}")


entry = Entry()
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

output = Label(text="0", font=("Times New Roman", 10, "normal"))
output.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=Convert_to_km)
button.grid(column=1, row=2)
















window.mainloop()
