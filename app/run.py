from subprocess import call
import webbrowser
import shlex
import customtkinter
from main import *
import os
import config
import threading
from datetime import datetime

def executeCommand(i, count):
    try :
        configCommand = shlex.split("python3 generateConfig.py")
        # sub.run(shlex.split(i))
        threading.Thread(target=call, args=(shlex.split(i) ,), ).start()
        threading.Thread(target=call, args=(shlex.split(configCommand) ,), ).start()
  
    except:
        print("Check that you have permissions to run the file, the file is in the correct path and it is an executable.")
# def create a popup window with single entry 
def userguide():
   webbrowser.open_new("https://github.com/jhjhajh/dso/blob/main/README.md")

# for testing if button works
def button_event():
    print("Button pressed")
        
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

def start():
    try:
        config.names=[]
        config.files=[]
        if os.path.isfile('data.txt'):
            with open('data.txt', 'r') as f:
                tempFiles = f.read()
                tempFiles = tempFiles.splitlines()
                for temp in tempFiles:
                    temp=temp.split(',')
                    config.names += [temp[0]]
                    config.files += [temp[1]]
    except:
        print("unable to read file. check the format of data file")

def write_frame_right(frame_right):
    label_info_1 = customtkinter.CTkLabel(master=frame_right,
                                                   text="Adversary Emulation\n",
                                                   height=100,
                                                   width = frame_right.winfo_screenwidth()/2,
                                                   text_font = ("Roboto Medium", 14),
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.CENTER)
    label_info_1.grid(column=0, row=0, sticky="n", padx=10, pady=10)
    x = 3
    i = ""
    count = 0
    for name in config.names:
        i=config.files[count]
        config.index_name=config.names[count]
        label = customtkinter.CTkLabel(master=frame_right, text=(name + ":"))
        label.grid(row=x, column=0, pady=0, padx=0, sticky="w")
        button = customtkinter.CTkButton(master=frame_right,
                                                text="Start",
                                                command=lambda i = i:executeCommand(i, count))                                                
        button.grid(row=x, column=0, pady=5, padx=0)
        x+=1
        count+=1
        
def refresh(frame_right):
    start()
    for widget in frame_right.winfo_children():
        widget.destroy()
    write_frame_right(frame_right)