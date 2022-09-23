import subprocess as sub
import webbrowser
import shlex
import customtkinter
from main import *
import os
import config

def executeCommand(i):
    sub.run(shlex.split(i))

def userguide():
   webbrowser.open_new("https://github.com/jhjhajh/dso/blob/main/README.md")

# for testing if button works
def button_event():
    print("Button pressed")
        
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

def start():
    config.names=[]
    config.files=[]
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
        label = customtkinter.CTkLabel(master=frame_right, text=(name + ":"))
        label.grid(row=x, column=0, pady=0, padx=0, sticky="w")
        button = customtkinter.CTkButton(master=frame_right,
                                                text="Start",
                                                command=lambda i = i:executeCommand(i))                                                
        button.grid(row=x, column=0, pady=5, padx=0)
        x+=1
        count+=1
        
def refresh(frame_right):
    start()
    for widget in frame_right.winfo_children():
        widget.destroy()
    write_frame_right(frame_right)