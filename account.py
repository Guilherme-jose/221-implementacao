import smtplib
from email.mime.text import MIMEText
import random

class account:
    def __init__(self, username='', password='', email='', phone_number='', verified=False):
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.verified = verified
        
        
    def __str__(self):
        return f"Username: {self.username}, Password: {self.password}, Email: {self.email}, Phone Number: {self.phone_number}"
    
    def generate_verification_code(self):
        verification_code = str(random.randint(1000, 9999))
        return verification_code
    
    def send_verification_email(self):
        # Code to send a verification email
        sender_email = "verumcarboapp@gmail.com"
        receiver_email = self.email
        subject = "Account Verification"
        message = "Código de verificação: \n\n" + self.generate_verification_code() + '\n'
        
        # Create a MIMEText object with the message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        
        # currently broken, google blocks 'less secure apps'
        
        #with smtplib.SMTP('smtp.gmail.com', 587) as server:
        #    server.starttls()
        #    server.login(sender_email, "verumCarbo-1408")
        #    server.send_message(msg)

    def login(self, username, password):
        f = open('accounts.txt', 'r')
        lines = f.readlines()
        f.close()
       
        for line in lines:
            data = line.split(', ')
            if data[0] == username and data[1] == password:
                self.username = username
                self.password = password
                self.email = data[2]
                self.phone_number = data[3]
                
                print(f"Logged in as {username}!")
                return True
        print("Login failed!")
        return False
               
    def register(self, username, password, email, phone_number):
        if(username == "" or password == "" or email == "" or phone_number == "" 
           or len(password) < 4 or '@' not in email or '.' not in email or 
            (len(phone_number) != 10 and len(phone_number) != 11)) : 
            return False
        else :
            print(f"Registering as {username}...")
            
            with open('accounts.txt', 'a') as f:
                f.write(f"{username}, {password}, {email}, {phone_number}\n")

            with open('users.txt', 'a') as f:
                f.write(f"{username}, ")
            
            self.send_verification_email()
            return True
        
    