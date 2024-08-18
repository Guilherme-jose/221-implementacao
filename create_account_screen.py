import tkinter as tk
from account import account
from screen import screen
from main_screen import main_screen

class create_account_screen(screen):
    def __init__(self, root):
        self.root = root
    
        
    def check_fields(self, username, password, email, phone_number):
        if len(password) < 4:
            self.pop_up('Senha muito curta')
            return False
        if username == '' or email == '' or phone_number == '':
            self.pop_up('Campos vazios')
            return False
        if '@' not in email or '.' not in email:
            self.pop_up('Email inválido')
            return False
        if len(phone_number) != 10 and len(phone_number) != 11:
            self.pop_up('Número de telefone inválido')
            return False
        
        
        
        return True
        
    def create_account(self):
        if self.check_fields(self.username_entry.get(), self.password_entry.get(), self.email_entry.get(), self.phone_number_entry.get()):
            acc = account(self.username_entry.get(), self.password_entry.get(), self.email_entry.get(), self.phone_number_entry.get())
            acc.register()
            
            
            self.hide()
            main = main_screen(self.root)
            main.show()
            
            self.pop_up('Conta criada com sucesso')
        
    def show(self):
        # Create the username label and entry field
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        # Create the password label and entry field
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()

        # Create the email label and entry field
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        # Create the phone number label and entry field
        self.phone_number_label = tk.Label(self.root, text="Phone Number:")
        self.phone_number_label.pack()
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.pack()

        # Create the create account button
        self.create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_button.pack()
        
        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=10)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.email_label.pack(pady=10)
        self.email_entry.pack(pady=10)
        self.phone_number_label.pack(pady=10)
        self.phone_number_entry.pack(pady=10)
        self.create_account_button.pack(pady=10)
    
    def hide(self):
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.email_label.pack_forget()
        self.email_entry.pack_forget()
        self.phone_number_label.pack_forget()
        self.phone_number_entry.pack_forget()
        self.create_account_button.pack_forget()