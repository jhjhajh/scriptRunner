import customtkinter
from add import *
import config
from tkinter import * 
import os
from run import *

def add_emulation():
    config.select = ""
    window = customtkinter.CTkToplevel()
    window.geometry("600x300")
    window.title("Add Emulation Flow")
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=2)
    window.grid_rowconfigure((0,1,4,5), weight=1)
    window.grid_rowconfigure((1,2), weight=2)
    
    label_name = customtkinter.CTkLabel(master=window, text="Enter Flow Name:")
    label_name.grid(row=1, column=0, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="ne")  
    entry_name = customtkinter.CTkEntry(master=window,
                                     placeholder_text="Name",
                                     height=30,
                                     width = 200,
                                     border_width=2,
                                     corner_radius=10)
                             
    entry_name.grid(row=1, column=1, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="nw")  
    
    label_file = customtkinter.CTkLabel(master=window, text="Add File for Emulation")
    label_file.grid(row=2, column=0, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="ne")  
    add_file_button = customtkinter.CTkButton(master=window,
                                             text="Select File",
                                             border_width=2,  # <- custom border_width
                                             fg_color=None,  # <- no fg_color
                                            command=lambda: (addFile(window))
                                             )
    add_file_button.grid(row=2, column=1, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="nw") 
    add_button = customtkinter.CTkButton(master=window,
                                             text="Add",
                                             border_width=2,  # <- custom border_width
                                             fg_color=None,  # <- no fg_color
                                             command=lambda:appendList(entry_name.get())
                                             )
    add_button.grid(row=5, column=1, columnspan=2, pady=20, padx=20, sticky="se")
    done_button = customtkinter.CTkButton(master=window,
                                             text="Done",
                                             border_width=2,  # <- custom border_width
                                             fg_color=("white", "gray38"),  # <- no fg_color
                                             command=window.destroy
                                             )
    done_button.grid(row=5, column=0, columnspan=2, pady=20, padx=20, sticky="sw")

def configure_window():
    window = customtkinter.CTkToplevel()
    window.geometry("600x300")
    window.title("Configure")
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=2)
    window.grid_rowconfigure((0,1,4,5), weight=1)
    window.grid_rowconfigure((1,2), weight=2)
    
    label_name = customtkinter.CTkLabel(master=window, text="Index Name:")
    label_name.grid(row=1, column=0, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="ne")  
    input_name = customtkinter.CTkEntry(master=window,
                                     placeholder_text=config.index_name,
                                     height=30,
                                     width = 200,
                                     border_width=2,
                                     corner_radius=10)
                             
    input_name.grid(row=1, column=1, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="nw")  
    label_ip = customtkinter.CTkLabel(master=window, text="IP Address:")
    label_ip.grid(row=2, column=0, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="ne")  
    ip = customtkinter.CTkEntry(master=window,
                                     placeholder_text=config.ip_addr,
                                     height=30,
                                     width = 200,
                                     border_width=2,
                                     corner_radius=10)
                             
    ip.grid(row=2, column=1, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="nw")     
    label_path = customtkinter.CTkLabel(master=window, text="Path: ")
    label_path.grid(row=3, column=0, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="ne")  
    path = customtkinter.CTkEntry(master=window,
                                     placeholder_text=config.path,
                                     height=30,
                                     width = 200,
                                     border_width=2,
                                     corner_radius=10)
                             
    path.grid(row=3, column=1, pady=0, padx=20, columnspan = 1, rowspan=4,sticky="nw")    
    done_button = customtkinter.CTkButton(master=window,
                                             text="Done",
                                             border_width=2,  # <- custom border_width
                                             fg_color=("white", "gray38"),  # <- no fg_color
                                             command=window.destroy
                                             )
    done_button.grid(row=5, column=0, columnspan=2, pady=20, padx=20, sticky="sw")   
    apply_button = customtkinter.CTkButton(master=window,
                                             text="Apply",
                                             border_width=2,  # <- custom border_width
                                             fg_color=("white", "gray38"),  # <- no fg_color
                                             command=lambda:(configure(input_name.get(), ip.get(), path.get()))
                                             )
    apply_button.grid(row=5, column=2, columnspan=2, pady=20, padx=20, sticky="sw")
