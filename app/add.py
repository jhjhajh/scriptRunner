from tkinter import filedialog
import config
import customtkinter
    

def addFile(window):
    config.select_file = filedialog.askopenfilename(initialdir="/home/kali", title="Select File", 
    filetypes=(("jupyter notebook", "*.ipynb"), ("all files", "*.*")))
    print(config.select_file)
    if config.select_file:
        label_2 = customtkinter.CTkLabel(master=window, text=config.select_file)
        label_2.grid(row=3, column=1, pady=0, padx=20, columnspan = 1, sticky="nw")
        
def appendList(entry_name):
    config.names += [entry_name]
    if (isJupyter()):
        config.files += ["jupyter notebook " + config.select_file] # only for jupyter notebooks
    else:
        config.files += [config.select_file]
    print(config.names)
    print(config.files)

def isJupyter():
    if (config.select_file.endswith("ipynb")):
        return True
    else:
        return False