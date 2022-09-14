import subprocess as sub
import webbrowser
import shlex
import customtkinter

def add_emulation():
    window = customtkinter.CTkToplevel()
    window.geometry("600x300")
    window.title("Add Emulation Flow")
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=2)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)         
    label_mode = customtkinter.CTkLabel(master=window, text="Enter Flow Name:")
    label_mode.grid(row=1, column=0, pady=0, padx=20, rowspan = 1, sticky="nw")        
    entry_1 = customtkinter.CTkEntry(master=window,
                                     placeholder_text="Name",
                                     width=120,
                                     height=25,
                                     border_width=2,
                                     corner_radius=10)
    entry_1.grid(row=1, column=1, columnspan=1, rowspan=3, pady=0, padx=20, sticky="nw")    

    lab = customtkinter.CTkLabel(master=window, text="Enter File Path:")
    lab.grid(row=2, column=0, pady=0, padx=20, sticky="nw")          
    entry_2 = customtkinter.CTkEntry(master=window,
                                     placeholder_text="File Path",
                                     width=120,
                                     height=25,
                                     border_width=2,
                                     corner_radius=10)
    entry_2.grid(row=2, column=1, columnspan=1, rowspan = 2, pady=0, padx=20, sticky="nw")                 
    add_button = customtkinter.CTkButton(master=window,
                                             text="Add",
                                             border_width=2,  # <- custom border_width
                                             fg_color=None,  # <- no fg_color
                                             # command = to work on add emulation command
                                             )
    add_button.grid(row=3, column=1, columnspan=1, pady=20, padx=20, sticky="se")
