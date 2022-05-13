from tkinter import *
from PIL import Image, ImageTk
import ingresoSinTarjeta,ingresoConTarjeta,ingresarTarjeta

class MenuPrincipal:
    def __init__(self,window):
        self.window= window
        self.window.geometry("1250x580")
        self.window.resizable(0,0)
        self.window.title("Cajero Automatico Bancolombia")
        self.window.iconbitmap('view/imagenes/LogoBancolombia.ico')
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
        MenuPrincipalBtIngresarTarjeta= Button(self.window, padx=25,border=0, pady=15, bg="#DD5222", command=self.go_IngresoTarjeta)
        MenuPrincipalBtIngresarTarjeta.place(x=15,y=435)

        MenuPrincipalBtIngresarSinTarjeta= Button(self.window, padx=25,border=0, pady=15, bg="#DD5222",command=self.go_IngresoTarjeta)
        MenuPrincipalBtIngresarSinTarjeta.place(x=1175,y=435)

    def go_IngresarTarjeta(self):
        win=Tk()
        ingresarTarjeta.IngresarTarjeta(win)
        #self.window.withdraw()
        self.window.destroy()
        win.deiconify()

    def go_IngresoTarjeta(self):
        win=Toplevel()
        ingresoSinTarjeta.MenuAccesoSinTarjeta(win)
        self.window.withdraw()
        win.deiconify()

def page():
    window= Tk()
    MenuPrincipal(window)
    window.mainloop()

if __name__ == "__main__":
    page()