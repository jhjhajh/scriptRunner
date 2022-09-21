from configparser import ConfigParser
import tkinter
import tkinter.messagebox
import customtkinter
import subprocess as sub
from tkinter import *
from run import *
from popup import *
import config

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 1000
    HEIGHT = 700

    def __init__(self):
        super().__init__()
        start()

        self.title("Adversary Emulation")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_sidebar = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Side Bar",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_sidebar.grid(row=1, column=0, pady=10, padx=10)

        self.button_closeApp = customtkinter.CTkButton(master=self.frame_left,
                                                text="Close App",
                                                command=self.on_closing)
        self.button_closeApp.grid(row=2, column=0, pady=10, padx=20)

        self.button_AddFlow = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Emulation",
                                                border_width=2,
                                                fg_color=None,
                                                command=add_emulation)
        self.button_AddFlow.grid(row=3, column=0, pady=10, padx=20)
        self.button_AddFlow = customtkinter.CTkButton(master=self.frame_left,
                                                text="Refresh",
                                                border_width=2,
                                                fg_color=None)
                                                #command=self.refresh(self.frame_right))
        self.button_AddFlow.grid(row=4, column=0, pady=10, padx=20)
        
        self.button_readme = customtkinter.CTkButton(master=self.frame_left,
                                                text="User Guide",
                                                command=userguide)
        self.button_readme.grid(row=8, column=0, pady=10, padx=20)
        
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)


        # ============ frame_info ============
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Adversary Emulation\n",
                                                   height=90,
                                                   width = self.frame_right.winfo_screenwidth()/3*2,
                                                   text_font = ("Roboto Medium", 14),
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.CENTER)
        self.label_info_1.grid(column=0, row=0, sticky="n", padx=10, pady=10)
        x = 1
        i = ""
        count = 0
        for name in config.names:
            i=config.files[count]
            self.label = customtkinter.CTkLabel(master=self.frame_right, text=(name + ":"))
            self.label.grid(row=x, column=0, pady=0, padx=0, sticky="w")
            self.button = customtkinter.CTkButton(master=self.frame_right,
                                                text="Start",
                                                command=lambda i = i:executeCommand(i))                                                
            self.button.grid(row=x, column=0, pady=5, padx=0)

            x+=1
            count+=1
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Add Emulation:", 
                                                        text_font=("Roboto Medium", -16))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # set default values
        self.optionmenu_1.set("Dark")
    def on_closing(self, event=0):
        x = len(config.names)
        with open('data.txt', 'w') as f:
            for i in range(x):
                f.write(config.names[i] + ',' + config.files[i]+'\n')
        self.destroy()
    def refresh(self, frame_right):
        self.frame_right.destroy()
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Adversary Emulation\n",
                                                   height=100,
                                                   width = self.frame_right.winfo_screenwidth()/2,
                                                   text_font = ("Roboto Medium", 14),
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.CENTER)
        self.label_info_1.grid(column=0, row=0, sticky="n", padx=10, pady=10)
        x = 3
        i = ""
        count = 0
        for name in config.names:
            i=config.files[count]
            self.label = customtkinter.CTkLabel(master=self.frame_right, text=(name + ":"))
            self.label.grid(row=x, column=0, pady=0, padx=0, sticky="w")
            self.button = customtkinter.CTkButton(master=self.frame_right,
                                                text="Start",
                                                command=lambda i = i:executeCommand(i))                                                
            self.button.grid(row=x, column=0, pady=5, padx=0)

            x+=1
            count+=1

if __name__ == "__main__":
    app = App()
    app.mainloop()
