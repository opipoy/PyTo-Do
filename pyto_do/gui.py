import customtkinter as ctk
from typing import Literal

class window(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = '#19193c')

    def mkbutton(self, x:int, y:int, text, color = '#a281d9', anchor_place = 'center', is_rel = True, **kwargs):
        b = ctk.CTkButton(self, fg_color=color, text=text, hover_color='#423459', **kwargs)

        b.place(**{'relx':x, 'rely':y, 'anchor':anchor_place} if is_rel else {'x':x, 'y':y, 'anchor':anchor_place})
        
        return b
    
    def make_frame(self):
        class file_scrollable_frame(ctk.CTkScrollableFrame):
            def __init__(self, master:ctk.CTk):
                super().__init__(master=master)
                self.checkboxes = []

            def add_option(self, cmd ,place, text:str):
                checkbox = ctk.CTkCheckBox(self, text=text, command=cmd)
                checkbox.grid(row=place[0], column=place[1])
                self.checkboxes.append(checkbox)
                return checkbox
            
            def get_checked_items(self):
                return [checkbox.cget("text") for checkbox in self.checkboxes if checkbox.get() == 1]
            
    
        return file_scrollable_frame(self)
  def make_todo(self, task_name, status):
