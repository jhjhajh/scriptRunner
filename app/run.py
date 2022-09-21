import subprocess as sub
import webbrowser
import shlex
import customtkinter
from main import *
import os
import config

def executeCommand(i):
    # print(i)
    # sub.run(shlex.split("jupyter-notebook /home/kali/Desktop/testnb.ipynb"))
    sub.run(shlex.split(i))
    # sub.run(i)
def userguide():
   webbrowser.open_new("https://github.com/jhjhajh/dso/blob/main/README.md")

def button_event():
    print("Button pressed")
        
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

def start():
     if os.path.isfile('data.txt'):
            with open('data.txt', 'r') as f:
                tempFiles = f.read()
                tempFiles = tempFiles.splitlines()
                # tempFiles=[x for x in tempFiles if x.strip()]
                # print(tempFiles)
                for temp in tempFiles:
                    temp=temp.split(',')
                    config.names += [temp[0]]
                    config.files += [temp[1]]
def refresh(frame_right):
    x = 1
    i = ""
    count = 0
    for name in config.names:
        i=config.files[count]
        label = customtkinter.CTkLabel(frame_right, text=(name + ":"))
        label.grid(row=x, column=0, pady=0, padx=0, sticky="w")
        button = customtkinter.CTkButton(master=frame_right,
                                            text="Start",
                                            command=lambda i = i:executeCommand(i))                                                
        button.grid(row=x, column=0, pady=5, padx=0)
        x+=1
        count+=1