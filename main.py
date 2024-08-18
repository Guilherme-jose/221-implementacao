import tkinter as tk
from login_screen import login_screen
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0')


root = tk.Tk()

root.geometry("1600x900")

login = login_screen(root)

login.show()

root.mainloop()
