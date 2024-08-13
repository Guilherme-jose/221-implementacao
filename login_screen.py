import tkinter as tk
from create_account_screen import create_account_screen
from account import account
from screen import screen

class login_screen(screen):
    def __init__(self, root):
        self.root = root
         
    def login(self):
        acc = account(self.username_entry.get(), self.password_entry.get())
        acc.login()
    
    def create_account(self):
        self.hide()
        ca_screen = create_account_screen(self.root)
        ca_screen.show()
        
    
    def hide(self):
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()
        self.create_account_button.pack_forget()
        
    def show(self):
        # Create the username label and entry field
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        # Create the password label and entry field
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        # Create the login button
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()



        # Create the create account button
        self.create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_button.pack()

        self.root.pack_propagate(0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)



        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=10)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.login_button.pack(pady=10)
        self.create_account_button.pack(pady=10)

