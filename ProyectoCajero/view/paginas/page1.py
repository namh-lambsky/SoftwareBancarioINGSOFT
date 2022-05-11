from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class Page1:

    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.geometry("1250x580")
        self.ventana.rowconfigure(0,weight=1)
        self.ventana.columnconfigure(0,weight=1)
        self.ventana.resizable(0,0)
        #self.ventana.state("zoomed")
        fondo= ImageTk.PhotoImage(Image.open("VIEW/imagenes/Pantallaprincipal.png"))

        MenuPrincipalFondo = Label(self.ventana, image=fondo)
        MenuPrincipalFondo.place(x=0,y=0)

        #botones
        MenuPrincipalBtIngresarTarjeta= Button(self.ventana, padx=25,border=0, pady=15, bg="#DD5222")
        MenuPrincipalBtIngresarTarjeta.place(x=15,y=435)

        MenuPrincipalBtIngresarSinTarjeta= Button(self.ventana, padx=25,border=0, pady=15, bg="#DD5222")
        MenuPrincipalBtIngresarSinTarjeta.place(x=1175,y=435)


def page():
    ventana= Tk()
    Page1(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    page()