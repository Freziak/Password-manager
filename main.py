from re import search
from tkinter import *
from random import randint, choice
from tkinter import messagebox
import json
MAIL = "danielmorawski04@gmail.com"

#Generate password
def generate_password():
    """Zwraca losowo wygenerowanie haslo skladajace sie z conajmniej 8 liter, 2 cyfr i 2 znakow specjalnych w losowej kolejnosci"""
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    password = "".join(password_list)
    password_entry.insert(0, password)

#Function save to files
def save():
    """Zapisuje dane takie jak strona email i haslo do pliku data.json, gdy taki plik nie istnieje tworzy go"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }

    if len(website) == 0 and len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    password_entry.delete(0, END)
#Find password
def find_password():
    """Szuka w pliku data.json hasla przypisanego do strony. Zwraca informacje w okienku gdy nie znajdzie powiazanego hasla lub calego pliku"""
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]['email']
            password = data[website]['password']
            if website in data:
                messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists.")
#Interface
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='./logo.png')
canvas.create_image(130, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string=MAIL)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(row=1, column=2)
window.mainloop()