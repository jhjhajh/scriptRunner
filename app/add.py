import subprocess as sub
import webbrowser
import shlex
import customtkinter
import tkinter as tk
from tkinter import filedialog, Text
import os

def addFlow(entry_name, entry_file):
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("jupyter notebook", "*.ipynb"), ("all files", "*.*")))
    print(entry_name, entry_file)

def addFile():
    select_file = filedialog.askopenfilename(initialdir="/home/kali", title="Select File", 
    filetypes=(("jupyter notebook", "*.ipynb"), ("all files", "*.*")))
    print(select_file)
