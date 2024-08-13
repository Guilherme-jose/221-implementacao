import tkinter as tk
from create_account_screen import create_account_screen

class login_screen():
    def __init__(self, root):
        self.root = root
         
    def login(self):
        pass
    
    def create_account(self):
        ca_screen = create_account_screen(self.root)
        ca_screen.show()
    
    def show(self):
        # Create the username label and entry field
        username_label = tk.Label(self.root, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        # Create the password label and entry field
        password_label = tk.Label(self.root, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        # Create the login button
        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.pack()



        # Create the create account button
        create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        create_account_button.pack()

        self.root.pack_propagate(0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        username_label.pack(pady=10)
        username_entry.pack(pady=10)
        password_label.pack(pady=10)
        password_entry.pack(pady=10)
        login_button.pack(pady=10)
        create_account_button.pack(pady=10)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)