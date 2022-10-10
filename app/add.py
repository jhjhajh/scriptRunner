from tkinter import filedialog
import config
import customtkinter
from run import *
import ipaddress

def addFile(window):
    config.select_file = filedialog.askopenfilename(initialdir="/home/kali/Desktop/DSO/app", title="Select File", 
    filetypes=(("jupyter notebook", "*.ipynb"), ("exe", "*.exe"), ("script", "*.sh"), ("all files", "*.*")))
    print(config.select_file)
    if config.select_file:
        label_2 = customtkinter.CTkLabel(master=window, text=config.select_file)
        label_2.grid(row=3, column=1, pady=0, padx=20, columnspan = 1, sticky="nw")
        
def configure(name, ip, path):
    # enure inputs are valid, config wont change unless valid
    if ((name.strip() != "") or (name.strip().isalnum())):
        config.index_name = name.strip()
    if (ip.strip() != ""):
        try:
            ip = ipaddress.ip_address(ip.strip())
            config.ip_addr = ip
        except:
            config.ip_addr = config.ip_addr
    if (path.strip() != ""):
        config.path = path
    print(config.index_name)
    print(config.ip_addr)
    print(config.path)
    

def appendList(entry_name):
    if entry_name == "":
        print("Please input flow name")
        errorwindow=customtkinter.CTkToplevel()
        errorwindow.geometry("200x100")
        errorwindow.title("Error")
        error_message = customtkinter.CTkLabel(master=errorwindow, text="Please input flow name")
        error_message.grid(row=0, column=0, pady=30, sticky="ew", padx=20)  
        errorwindow.after(2000, lambda: errorwindow.destroy())
    elif config.select_file == "":
        print("Please select a file")
        errorwindow=customtkinter.CTkToplevel()
        errorwindow.geometry("280x100")
        errorwindow.title("Error")
        error_message = customtkinter.CTkLabel(master=errorwindow, text="\n\tPlease select a file")
        error_message.grid(row=0, column=0, pady=0, sticky="ew", padx="20")  
        errorwindow.after(2000, lambda: errorwindow.destroy())
    elif not entry_name.isalnum():
        # print("please try again")
        # errorwindow=customtkinter.CTkToplevel()
        # errorwindow.geometry("280x10")
        # errorwindow.title("Error")
        # error_message = customtkinter.CTkLabel(master=errorwindow, text="\nPlease only use alphanumeric characters and" + "\n" +" spaces in emulation name")
        # error_message.grid(row=0, column=0, pady=0,  sticky="ew")  
        # errorwindow.after(3000, lambda: errorwindow.destroy())
        print("Please use alphanumeric characters without spaces in emulation name")
        errorwindow=customtkinter.CTkToplevel()
        errorwindow.geometry("300x100")
        errorwindow.title("Error")
        error_message = customtkinter.CTkLabel(master=errorwindow, text="\nPlease use alphanumeric characters without" + "\n" +" spaces in emulation name")
        error_message.grid(row=0, column=0, pady=0, sticky="ew", padx="20")  
        errorwindow.after(2000, lambda: errorwindow.destroy())

    else:
        config.names += [entry_name]
        if (isJupyter()):
            config.files += ["jupyter notebook " + config.select_file]
        elif (isPython()):
            config.files += ["python3 " + config.select_file]
        else:
            config.files += [config.select_file]
        print(config.names)
        print(config.files)
        save_file()
        print("flow added")
        successWindow=customtkinter.CTkToplevel()
        successWindow.geometry("200x100")
        successWindow.title("Success")
        error_message = customtkinter.CTkLabel(master=successWindow, text="\nSuccess, flow added!\nRefresh to apply")
        error_message.grid(row=0, column=0, pady=0, sticky="ew", padx="20")  
        successWindow.after(2000, lambda: successWindow.destroy())
        


def isJupyter():
    if (config.select_file.endswith("ipynb")):
        return True
    else:
        return False
        
def isPython():
    if (config.select_file.endswith("py")):
        return True
    else:
        return False

def save_file():
    try:
        x = len(config.names)
        with open('data.txt', 'w') as f:
            f.write(config.index_name + '\n')
            f.write(config.ip_addr + '\n')
            f.write(config.path + '\n')
            for i in range(x):
                f.write(config.names[i] + ',' + config.files[i]+'\n')
    except:
        print("unable to save file. check if data file is corrupted")