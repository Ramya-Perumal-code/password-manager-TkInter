from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_psd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_edit.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_edit.get()
    user = user_edit.get()
    psd = password_edit.get()
    if web == '' or psd == '':
        messagebox.showerror(title="Error", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {user}"
                                                          f"\nPassword: {psd} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{web} | {user}| {psd}\n")

                website_edit.delete(0, 'end')
                password_edit.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=190)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=photo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_edit = Entry(width=35)
website_edit.grid(row=1, column=1, columnspan=2)
website_edit.focus()

user_edit = Entry(width=35)
user_edit.grid(row=2, column=1, columnspan=2)
user_edit.insert(0, "Ramya.chn@gmail.com")

password_edit = Entry(width=21)
password_edit.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", command=generate_psd)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()

