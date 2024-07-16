import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

class GUI():
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_generatedpassword = StringVar()
        self.n_passwordlen = IntVar()
        
        root.title('Password Generator')
        root.geometry('660x500')
        root.config(bg='#F0F0F0')  # Light gray background
        root.resizable(False, False)

        self.label = Label(text="PASSWORD GENERATOR", anchor=N, fg='#68228B', bg='#F0F0F0', font='Arial 20 bold underline')
        self.label.grid(row=0, column=1, pady=20)

        self.user = Label(text="Enter User Name:", font='Arial 15 bold', bg='#F0F0F0', fg='#68228B')
        self.user.grid(row=1, column=0, padx=20, pady=10, sticky=E)

        self.textfield = Entry(textvariable=self.n_username, font='Arial 15', bd=6, relief='ridge')
        self.textfield.grid(row=1, column=1, padx=20, pady=10, sticky=W)
        self.textfield.focus_set()

        self.length = Label(text="Enter Password Length:", font='Arial 15 bold', bg='#F0F0F0', fg='#68228B')
        self.length.grid(row=2, column=0, padx=20, pady=10, sticky=E)

        self.length_textfield = Entry(textvariable=self.n_passwordlen, font='Arial 15', bd=6, relief='ridge')
        self.length_textfield.grid(row=2, column=1, padx=20, pady=10, sticky=W)
        
        self.generated_password = Label(text="Generated Password:", font='Arial 15 bold', bg='#F0F0F0', fg='#68228B')
        self.generated_password.grid(row=3, column=0, padx=20, pady=10, sticky=E)

        self.generated_password_textfield = Entry(textvariable=self.n_generatedpassword, font='Arial 15', bd=6, relief='ridge', fg='#DC143C')
        self.generated_password_textfield.grid(row=3, column=1, padx=20, pady=10, sticky=W)
   
        self.generate = Button(text="Generate Password", bd=3, relief='raised', padx=10, pady=5, font='Arial 12 bold', fg='#FFFFFF', bg='#68228B', command=self.generate_pass)
        self.generate.grid(row=4, column=1, padx=20, pady=20)

        self.accept = Button(text="Accept", bd=3, relief='raised', padx=10, pady=5, font='Arial 12 bold', fg='#FFFFFF', bg='#458B00', command=self.accept_fields)
        self.accept.grid(row=5, column=1, padx=20, pady=10)

        self.reset = Button(text="Reset", bd=3, relief='raised', padx=10, pady=5, font='Arial 12 bold', fg='#FFFFFF', bg='#FF5733', command=self.reset_fields)
        self.reset.grid(row=6, column=1, padx=20, pady=10)

    def generate_pass(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        chars = "@#%&()\"?!"
        numbers = "1234567890"
        
        name = self.textfield.get()
        leng = self.length_textfield.get()

        if name == "":
            messagebox.showerror("Error", "Name cannot be empty")
            return

        if not name.isalpha():
            messagebox.showerror("Error", "Name must contain only alphabets")
            self.textfield.delete(0, END)
            return

        try:
            length = int(leng)
            if length < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters long")
                self.length_textfield.delete(0, END)
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid password length")
            self.length_textfield.delete(0, END)
            return

        upper = list(upper)
        lower = list(lower)
        chars = list(chars)
        numbers = list(numbers)

        u = random.randint(1, length-3)
        l = random.randint(1, length-2-u)
        c = random.randint(1, length-1-u-l)
        n = length-u-l-c

        password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers, n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        self.generated_password_textfield.delete(0, END)
        self.generated_password_textfield.insert(0, gen_passwd)

    def accept_fields(self):
        username = self.n_username.get().strip()
        generated_password = self.n_generatedpassword.get().strip()

        if username == "" or generated_password == "":
            messagebox.showerror("Error", "Please generate and enter a password")
            return

        try:
            with sqlite3.connect("users.db") as db:
                cursor = db.cursor()
                find_user = "SELECT * FROM users WHERE Username = ?"
                cursor.execute(find_user, (username,))
                if cursor.fetchone():
                    messagebox.showerror("Error", "This username already exists! Please use another username.")
                else:
                    insert_query = "INSERT INTO users(Username, GeneratedPassword) VALUES (?, ?)"
                    cursor.execute(insert_query, (username, generated_password))
                    db.commit()
                    messagebox.showinfo("Success", "Password generated and stored successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert into database: {e}")

    def reset_fields(self):
        self.n_username.set("")
        self.n_passwordlen.set("")
        self.n_generatedpassword.set("")
        self.textfield.focus_set()

if __name__=='__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()
