import tkinter as tk

class create_account_screen():
    def __init__(self, root):
        self.root = root
        
    def create_account(self):
        pass
    
    def show(self):
        # Create the email label and entry field
        email_label = tk.Label(self.root, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()
        
        # Create the phone number label and entry field
        phone_number_label = tk.Label(self.root, text="Phone Number:")
        phone_number_label.pack()
        phone_number_entry = tk.Entry(self.root)
        phone_number_entry.pack()
        
        # Create the create account button
        create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        create_account_button.pack()
        
        email_label.pack(pady=10)
        email_entry.pack(pady=10)
        phone_number_label.pack(pady=10)
        phone_number_entry.pack(pady=10)
        create_account_button.pack(pady=10)
        
        frame = tk.Frame(self.root)
        
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)