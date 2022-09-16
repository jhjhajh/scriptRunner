import subprocess as sub
import webbrowser
import shlex
import customtkinter

apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        print(tempApps)
        apps=[x for x in tempApps if x.strip()]

# add file instead of using file path?? or should just use file path idk but leave it here first
def addFile():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("jupyter notebook", "*.ipynb"), ("all files", "*.*"))
    apps.append(filename) 
    print(filename) #prints file path of file selected, maybe can use this to append as well, and use this function for people to select file instead of asking them to type since I can retrieve the file like that
# maybe only allow jupyter notebook for now
    for app in apps:
        label = tk.label(frame, text=app, bg="gray")
        label.pack()




# - populate the app[] from file, 
# - add to app[] during run time. need add an option to delete but see how first
# when app closing, overwrite the apps into text file upon closing
# after that maybe can use some dictionary to map the name and the file path where the name is the key. if the name input is the same either ovewrite the old one or just have duplicate or have error message, whichever is easier to deal with

for app in apps:
    label = tk.label(frame,text=app)
    label.pack()

# put under main or under the closing function
#with open('save.txt', 'w') as f:
#    for app in apps:
#        f.write(app + ',')



"""
    lab = customtkinter.CTkLabel(master=window, text="Enter File Path:")
    lab.grid(row=2, column=0, pady=0, padx=20, sticky="nw")          
    entry_file = customtkinter.CTkEntry(master=window,
                                     placeholder_text="File Path",
                                     width=120,
                                     height=25,
                                     border_width=2,
                                     corner_radius=10)
    entry_file.grid(row=2, column=1, columnspan=1, rowspan = 2, pady=0, padx=20, sticky="nw")
"""
