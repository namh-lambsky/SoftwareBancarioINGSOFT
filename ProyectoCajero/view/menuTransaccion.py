from tkinter import *
from PIL import Image, ImageTk
import menuPrincipal,ingresoConTarjeta, retirarDinero

class MenuTransaccion:
    def __init__(self,window):
        self.window= window
        self.window.geometry("1250x580")
        self.window.resizable(0,0)
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        #cargar imagen
        fondoMenuTransaccion= Image.open("VIEW/imagenes/MenuTransaccion.png")
        resizeImagef=fondoMenuTransaccion.resize((1250,580))
        fondoMenuTransaccion= ImageTk.PhotoImage(resizeImagef)
        #MenuTransaccion--------------------------------------------------------------------------

        menuTransaccionfondo=Label(self.window, image=fondoMenuTransaccion)
        menuTransaccionfondo.image=fondoMenuTransaccion
        menuTransaccionfondo.place(x=0,y=0)

        #botones MenuTransaccion
        menuTransaccionBtRetirarDinero= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDinero.place(x=25,y=147)

        menuTransaccionBtConsultarSaldo= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtConsultarSaldo.place(x=25,y=282)

        menuTransaccionBtTransferencias= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtTransferencias.place(x=1170,y=147)

        menuTransaccionBtFinalizar= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtFinalizar.place(x=25,y=417)

    def go_RetirarDineroMenu(self):
        win=Toplevel()
        retirarDinero.MenuRetirarDinero(win)
        self.window.withdraw()
        win.deiconify()

    def go_ConsultaDeSaldo(self):
        win=Toplevel()
        menuPrincipal.MenuPrincipal(win)
        self.window.withdraw()
        win.deiconify()

    def go_Transferencias(self):
        win=Toplevel()
        menuPrincipal.MenuPrincipal(win)
        self.window.withdraw()
        win.deiconify()

    def go_MainMenu(self):
        win=Toplevel()
        menuPrincipal.MenuPrincipal(win)
        self.window.withdraw()
        win.deiconify()

def page():
    window= Tk()
    MenuTransaccion(window)
    window.mainloop()

if __name__ == "__main__":
    page()