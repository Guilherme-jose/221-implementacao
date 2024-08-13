import tkinter as tk

class screen():
    def __init__(self, root):
        self.root = root
        
    def pop_up(self, message='Erro'):
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        
    def hide(self):
        pass
    
    def show(self):
        pass