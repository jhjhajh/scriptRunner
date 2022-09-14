import subprocess as sub
import webbrowser
import shlex

def run():
    sub.run(shlex.split("jupyter-notebook /home/kali/Desktop/testnb.ipynb"))
    
def userguide():
   webbrowser.open_new("https://github.com/jhjhajh/dso/blob/main/README.md")

#https://www.anycodings.com/1questions/1784012/run-linux-terminal-commands-from-python-gui-tkinter 
#to parse inputs
