import subprocess as sub
import webbrowser
import shlex
import customtkinter
from add import *

def add_emulation():

    window = customtkinter.CTkToplevel()
    window.geometry("600x300")
    window.title("Add Emulation Flow")
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=2)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)         
    label_1 = customtkinter.CTkLabel(master=window, text="Enter Flow Name:")
    label_1.grid(row=1, column=0, pady=0, padx=20, columnspan = 1, sticky="ne")  
    entry_name = customtkinter.CTkEntry(master=window,
                                     placeholder_text="Name",
                                     height=30,
                                     width = 200,
                                     border_width=2,
                                     corner_radius=10)
                             
    entry_name.grid(row=1, column=1, pady=0, padx=20, columnspan = 1, sticky="nw")  
    
    label_2 = customtkinter.CTkLabel(master=window, text="Add File for Emulation")
    label_2.grid(row=2, column=0, pady=0, padx=20, columnspan = 1, sticky="ne")  
    add_file_button = customtkinter.CTkButton(master=window,
                                             text="Select File",
                                             border_width=2,  # <- custom border_width
                                             fg_color=None,  # <- no fg_color
                                             command=addFile
                                             )
    add_file_button.grid(row=2, column=1, pady=0, padx=20, columnspan = 1, sticky="nw")
                                          
    add_button = customtkinter.CTkButton(master=window,
                                             text="Add",
                                             border_width=2,  # <- custom border_width
                                             fg_color=None,  # <- no fg_color
                                             #command=addFlow(entry_name, entry_file)
                                             )
    add_button.grid(row=2, column=1, columnspan=2, pady=20, padx=20, sticky="se")

