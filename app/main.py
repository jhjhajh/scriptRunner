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

        self.frame_right = customtkinter.CTkFrame(master=self, highlightthickness=0)
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
        self.button_refresh = customtkinter.CTkButton(master=self.frame_left,
                                                text="Refresh",
                                                border_width=2,
                                                fg_color=None,
                                                command=lambda:(refresh(self.frame_right)))

        self.button_refresh.grid(row=4, column=0, pady=10, padx=20)
        
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
            #     # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)
        write_frame_right(self.frame_right)
        
    def on_closing(self, event=0):
        save_file()
        self.destroy()

if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except:
        print("error opening app. please try again")
    finally:
        print("Thank you for using app. Bye :D")
