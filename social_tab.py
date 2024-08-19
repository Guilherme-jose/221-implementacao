from tkinter import Toplevel, ttk
import tkinter as tk
from tab import tab
from activity import activity

class social_tab(tab):
    def __init__(self, root, type='social'):
        super().__init__(root, type)
    
    def upload_file(self):
        pass
        
    def show(self):
        ttk.Label(self.root, text='Social Tab').pack()
        # Create a button to open the event screen
        open_event_button = ttk.Button(self.root, text='Open Event Screen', command=self.open_event_screen)
        open_event_button.pack()
        
        self.display_activities('social')
    
    
    