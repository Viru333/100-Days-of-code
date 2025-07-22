from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    generated_password = PasswordGenerator().generate_password()
    window.clipboard_clear()
    window.clipboard_append(generated_password)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry():
    website_name = website_entry.get()
    username = username_entry.get()
    password_input = password_entry.get()

    if len(website_name) == 0 or len(password_input) == 0:
        messagebox.showerror(title="Oops!", message="Please make sure you haven't left any field empty")

    else:
        new_data = {
            website_name: {
                "email": username,
                "password": password_input,
            },
        }

        try:
            with open("Manage Passwords.json", 'r') as f:
                # retrieve old data
                data = json.load(f) # dict type

        except FileNotFoundError:
            with open("Manage Passwords.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)
            with open("Manage Passwords.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            # Clearing text entered in entries
            website_entry.delete(0, END)
            # username_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():

    website_name = website_entry.get()
    if len(website_name) == 0:
        messagebox.showerror(title="Oops!", message="Please make sure you haven't left website field empty")
    else:
        try:
            # with open('Manage Passwords.json')
            f = open('Manage Passwords.json')

        except FileNotFoundError:
            messagebox.showerror(title="Oops!",message="No Data Files Found!!")

        else:
            # Finding password in data_storage
            data_storage = json.load(f)
            if website_name in data_storage:
                messagebox.showinfo(title=website_name, message=f"Username: {data_storage[website_name]["email"]}\n Password: {data_storage[website_name]["password"]}")

            else:
                messagebox.showerror(title="Oops!", message=f"No Details for {website_name} found!!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20, bg="white")
# window.minsize(300, 300)
window.title("Password Manager")
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
canvas.create_image(65, 100, image=lock_img)
canvas.grid(column=1, row=0, padx=5, pady=5)


# Labels
website = Label(window, text="Website:", bg="white")
website.grid(row=1, column=0, sticky=E, padx=5, pady=5)

user_name = Label(window, text="Email/Username:", bg="white")
user_name.grid(row=2, column=0, sticky=E, padx=5, pady=5)

password = Label(window, text="Password:", bg="white")
password.grid(row=3, column=0, sticky=E, padx=5, pady=5)


# Entries

website_entry = Entry(window, width=23, bg="white")
website_entry.grid(row=1, column=1, sticky=W, columnspan=1, padx=5, pady=5)
website_entry.focus()

username_entry = Entry(window, width=42, bg="white")
username_entry.insert(END, "aman902821@gmail.com")
username_entry.grid(row=2, column=1, sticky=W, columnspan=2, padx=5, pady=5)

password_entry = Entry(window, width=23, bg="white")
password_entry.grid(row=3, column=1, sticky=W, columnspan=2, padx=5, pady=5)


# Buttons
search = Button(window, text="Search", width=15, bg="white", highlightthickness=0, bd=1, command=search_password)
search.grid(row=1, column=1, columnspan=2, sticky=E, padx=5, pady=5)
generate_pass = Button(window, width=15, text="Generate Password", bg="white", highlightthickness=0, bd=1, command=get_password)
generate_pass.grid(row=3, column=1, columnspan=2, sticky=E, padx=5, pady=5)

add = Button(window, text="Add", width=35, bg="white", highlightthickness=0, bd=1, command=save_entry)
add.grid(row=4, column=1, sticky=W, columnspan=2, padx=5, pady=5)


window.mainloop()