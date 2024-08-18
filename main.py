import tkinter as tk
from login_screen import login_screen


root = tk.Tk()

root.geometry("1600x900")

login = login_screen(root)

login.show()

root.mainloop()
