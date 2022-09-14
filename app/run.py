import subprocess as sub
import webbrowser
import shlex
import customtkinter

def run():
    sub.run(shlex.split("jupyter-notebook /home/kali/Desktop/testnb.ipynb"))
    
def userguide():
   webbrowser.open_new("https://github.com/jhjhajh/dso/blob/main/README.md")

def button_event():
    print("Button pressed")
        
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)
