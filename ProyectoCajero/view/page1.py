from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
import page2


class Page1:
    def __init__(self,window):
        self.window= window
        self.window.geometry("1250x580")
        self.window.resizable(0,0)
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        #self.window.state("zoomed")
        #Imagenes
        #Cargar imagen fondo

        #MenuPrincipal---------------------------------------------------------
        MenuPrincipalFondo= Image.open("view/imagenes/Pantallaprincipal.png")
        resizeImagef=MenuPrincipalFondo.resize((1250,580))
        MenuPrincipalFondo= ImageTk.PhotoImage(resizeImagef)

        MenuPrincipalFondoLb= Label(self.window, image=MenuPrincipalFondo)
        MenuPrincipalFondoLb.image=MenuPrincipalFondo
        MenuPrincipalFondoLb.place(x=0,y=0)
        #botones
        MenuPrincipalBtIngresarTarjeta= Button(self.window, padx=25,border=0, pady=15, bg="#DD5222", command=self.go_page2)
        MenuPrincipalBtIngresarTarjeta.place(x=15,y=435)

        MenuPrincipalBtIngresarSinTarjeta= Button(self.window, padx=25,border=0, pady=15, bg="#DD5222")
        MenuPrincipalBtIngresarSinTarjeta.place(x=1175,y=435)

    def go_page2(self):
        win=Toplevel()
        page2.Page2(win)
        self.window.withdraw()
        #win.deiconify()

def page():
    window= Tk()
    Page1(window)
    window.mainloop()



if __name__ == "__main__":
    page()