from tkinter import *
from PIL import Image, ImageTk
from argparse import ZERO_OR_MORE
from ctypes import resize
from platform import win32_edition
import page1, page3


class Page2:
    def __init__(self,window):
        self.window= window
        self.window.geometry("1250x580")
        self.window.resizable(0,0)
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        #self.window.state("zoomed")
        #ingresarTarjeta---------------------------------------------------------
        fondoingresarTarjeta= Image.open("view/imagenes/2.png")
        resizeImagef=fondoingresarTarjeta.resize((1250,580))
        fondoingresarTarjeta= ImageTk.PhotoImage(resizeImagef)

        #ingresarTarjeta---------------------------------------------------------
        ingresarTarjetafondo=Label(self.window, image=fondoingresarTarjeta)
        ingresarTarjetafondo.image=fondoingresarTarjeta
        ingresarTarjetafondo.place(x=0,y=0)
        
        #botones ingresarTarjeta
        ingresarTarjetaBtIngresar= Button(self.window, padx=25,border=0, pady=15, bg="#7ed957", command=self.go_page1)
        ingresarTarjetaBtIngresar.place(x=100,y=345)

        ingresarTarjetaBt2Ingresar= Button(self.window, padx=25,border=0, pady=15, bg="#e61717", command=self.go_page1)
        ingresarTarjetaBt2Ingresar.place(x=100,y=445)


    def go_page3(self):
        win=Toplevel()
        page3.Page3(win)
        self.window.withdraw()
        #win.deiconify()

    def go_page1(self):
        win=Toplevel()
        page1.Page1(win)
        self.window.withdraw()
        #win.deiconify()


def page():
    window= Tk()
    Page2(window)
    window.mainloop()



if __name__ == "__main__":
    page()