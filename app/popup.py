import customtkinter
from add import *
import config
from tkinter import * 
import os

def add_emulation():

    window = customtkinter.CTkToplevel()
    window.geometry("600x300")
    window.title("Add Emulation Flow")
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=2)
    window.grid_rowconfigure(0, weight=3)
    window.grid_rowconfigure(0, weight=1)
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
                                            command=lambda: (addFile(window))
                                             )
    add_file_button.grid(row=2, column=1, pady=0, padx=20, columnspan = 1, sticky="nw")
        
    add_button = customtkinter.CTkButton(master=window,
                                             text="Add",
                                             border_width=2,  # <- custom border_width
                                             fg_color=None,  # <- no fg_color
                                             command=lambda:appendList(entry_name.get())
                                             )
    add_button.grid(row=4, column=1, columnspan=2, pady=20, padx=20, sticky="se")
    done_button = customtkinter.CTkButton(master=window,
                                             text="Done",
                                             border_width=2,  # <- custom border_width
                                             fg_color=("white", "gray38"),  # <- no fg_color
                                             command=window.destroy
                                             )
    done_button.grid(row=4, column=0, columnspan=2, pady=20, padx=20, sticky="sw")

def appendList(entry_name):
    config.names += [entry_name]
    config.files += ["jupyter notebook " + config.select_file] # only for jupyter notebooks
    print(config.names)
    print(config.files)
