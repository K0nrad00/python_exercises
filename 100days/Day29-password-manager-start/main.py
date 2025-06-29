import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for number in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password) # insert password into password field starting @ index 0, insert is python built in function
    pyperclip.copy(password) # copy to clipboard
# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear():
    web_entry.delete(0, "end")
    email_entry.delete(0, "end")
    email_entry.insert(0, "dummy@email.com")
    password_entry.delete(0, "end")

def save():
    website = web_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showinfo(title="Error: Field empty", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                      f"Email: {username}\n"
                                                      f"Password: {password}\n"
                                                      f"Confirm to save?")
        if is_ok:
            with open("password_data.txt", "a") as f:
                f.write(f"{website} | {username} | {password}\n")
            clear()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=320, height=320)

# Logo image
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label/entry
web_label = tkinter.Label(text="Website")
web_label.grid(column=0, row=1)
web_entry = tkinter.Entry(width=36)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

# Email/uname label/Entry
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = tkinter.Entry(width=36)
email_entry.insert(0, "dummy@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password label, entry, button:
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(width=20)
password_entry.grid(column=1, row=3)
password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

# Add button
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
