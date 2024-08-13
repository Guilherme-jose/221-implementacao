import smtplib
from email.mime.text import MIMEText
import random

class account:
    def __init__(self, username, password, email='', phone_number='', verified=False):
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
        sender_email = "guilherme.j.lopes@ufv.br"
        receiver_email = self.email
        subject = "Account Verification"
        message = "Código de verificação: \n\n" + self.generate_verification_code() + '\n'
        
        # Create a MIMEText object with the message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        
        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, "Ash&314ka2-101074")
            server.send_message(msg)

    def login(self):
        # Code to log the user in
        print(f"Logging in as {self.username}...")
    