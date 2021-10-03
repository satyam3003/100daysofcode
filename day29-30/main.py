from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

BLACK = '#000'
WHITE = '#FFFFFF'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0, 'end')
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_entry = {
        website: {
            'username': username,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Try Again', message='Please fill all input')
    else:
        popup_ok = messagebox.askokcancel(title=website,
                                          message=f'You have entered:\nusername: {username}\npassword: {password}\nDo you want to save this info?')
        if popup_ok:
            try:
                with open('day29-30/password_manager.json', mode='r') as file:
                    data = json.load(file)  # read the data from file
                    data.update(new_entry)  # update the data from file with new_entry
            except FileNotFoundError:
                data = new_entry

            with open('day29-30/password_manager.json', mode='w') as file:
                json.dump(data, file, indent=4)  # next we write the complete file with previous file + new entry

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            username_entry.insert(0, 'baldawasatyam30@gamil.com')
            website_entry.focus()


# ----------------------------Search Website -------------------------
def search_website():
    try:
        with open('day29-30/password_manager.json', mode='r') as file:
            search_dict = json.load(file)
            website = website_entry.get()
            try:
                messagebox.showinfo(title=website,
                                    message=f"username: {search_dict[website]['username']}\npassword: {search_dict[website]['password']}")
            except KeyError:
                messagebox.showinfo(title='Password not saved', message=f'password for {website} is not saved')
    except FileNotFoundError:
        messagebox.showinfo(title='Oops!', message='no passwords saved')
    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BLACK)

# Canvas config for image
canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
password_image = PhotoImage(file='day29-30/logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text='Website', pady=5, bg=BLACK, fg=WHITE)
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

website_search = Button(width=15, text='Search', command=search_website)
website_search.grid(row=1, column=2)

# username
username_label = Label(text='Email/Username', pady=5, bg=BLACK, fg=WHITE)
username_label.grid(row=2, column=0)

username_entry = Entry(width=55)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'baldawasatyam30@gamil.com')
# password
password_label = Label(text='Password', pady=5, bg=BLACK, fg=WHITE)
password_label.grid(row=3, column=0)

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

password_generator = Button(text='Generate Password', command=generate_password)
password_generator.grid(row=3, column=2)

# Add
add_button = Button(text='Add', width=46, command=add_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
