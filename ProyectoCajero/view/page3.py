from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
from argparse import ZERO_OR_MORE
from ctypes import resize
from platform import win32_edition
import page1


class Page3:
    def __init__(self,window):
        self.window= window
        self.window.geometry("1250x580")
        self.window.resizable(0,0)
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        #self.window.state("zoomed")


    def go_page4(self):
        win=Toplevel()
        page4.Page4(win)
        self.window.withdraw()
        #win.deiconify()

    def go_page1(self):
        win=Toplevel()
        page1.Page1(win)
        self.window.withdraw()
        #win.deiconify()

def page():
    window= Tk()
    Page3(window)
    window.mainloop()



if __name__ == "__main__":
    page()