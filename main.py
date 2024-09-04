import tkinter as tk
from login_screen import login_screen
import os

#if os.environ.get('DISPLAY','') == '':
    #print('no display found. Using :0.0')
    #os.environ.__setitem__('DISPLAY', ':0.0')


root = tk.Tk()

root.geometry("1600x900")

root.configure(bg='#1e3743')

root.option_add("*Label*Background", '#1e3743')

root.option_add("*Label*Foreground", 'white')

root.option_add("*Label.Font", "Arial 14")

login = login_screen(root)

login.show()

root.mainloop()
