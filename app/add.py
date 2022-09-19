from tkinter import filedialog
import config
import customtkinter

def addFlow(entry_name, entry_file):
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("jupyter notebook", "*.ipynb"), ("all files", "*.*")))
    print(entry_name, entry_file)

# def addFile(window):
def addFile():
    config.select_file = filedialog.askopenfilename(initialdir="/home/kali", title="Select File", 
    filetypes=(("jupyter notebook", "*.ipynb"), ("all files", "*.*")))
    print(config.select_file)
    # if config.select_file:
    #     label_2 = customtkinter.CTkLabel(master=window, text=config.select_file)
    #     label_2.grid(row=3, column=0, pady=0, padx=20, columnspan = 1, sticky="ne") 