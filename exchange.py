#!/bin/sh

import serial
import threading
import Queue as Queue
import Tkinter as tk
import time
import re
import tkMessageBox
from StringIO import StringIO 

from Tkinter import *
from PIL import Image

TITLE_FONT = ("Helvetica", 18, "bold")
BANK = 100
global state
state = 0 
    

class App(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        self.geometry("800x480")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        print "SUSSSSSSSSSSSSSSSSSSSs"
                    
        self.frames = {}
        for F in (WaitBank,StartPage):
            page_name = F.__name__
            print F.__name__
            frame = F(self.container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")



class StartPage(tk.Frame):   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = Canvas(self, width=800, height=480,bg="#C6E2FF")
        self.canvas.grid(row=0, column=0)

        
class WaitBank(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.sec = 0
        self.controller = controller
        self.canvas = Canvas(self, width=800, height=480,bg="#C6E2FF")
        self.canvas.grid(row=0, column=0)

        
        



app = App()
app.attributes('-fullscreen', True)
app.mainloop()
