import tkinter as tk
from create_account_screen import create_account_screen
from account import account
from screen import screen
from main_screen import main_screen

class login_screen(screen):
    def __init__(self, root):
        self.root = root
         
    def login(self):
        acc = account()
        if acc.login(self.username_entry.get(), self.password_entry.get()):
            self.hide()
            main = main_screen(self.root)
            main.show()
    
    def create_account(self):
        self.hide()
        ca_screen = create_account_screen(self.root)
        ca_screen.show()
        
    
    def hide(self):
        self.logo_label.grid_remove()
        self.username_label.grid_remove()
        self.username_entry.grid_remove()
        self.password_label.grid_remove()
        self.password_entry.grid_remove()
        self.login_button.grid_remove()
        self.create_account_button.grid_remove()
        
    def show(self):
        self.root.geometry('600x400')
        
        self.logo = tk.PhotoImage(file="logo.png")
        
        self.logo_label = tk.Label(self.root, image=self.logo)
        self.logo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        
        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.create_account_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.root.grid_columnconfigure((0,1), weight=1)
        self.root.grid_rowconfigure((10,0), weight=1)
    

