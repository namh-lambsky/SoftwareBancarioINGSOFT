from tkinter import *
from PIL import Image, ImageTk
import menuPrincipal

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

        MenuTransaccionfondo=Label(self.window, image=fondoMenuTransaccion)
        MenuTransaccionfondo.image=fondoMenuTransaccion
        MenuTransaccionfondo.place(x=0,y=0)

        #botones MenuTransaccion
        MenuTransaccionBtRetirarDinero= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        MenuTransaccionBtRetirarDinero.place(x=25,y=160)

        MenuTransaccionBtConsultarSaldo= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        MenuTransaccionBtConsultarSaldo.place(x=25,y=295)

        MenuTransaccionBtTransferencias= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        MenuTransaccionBtTransferencias.place(x=1170,y=160)



        def go_page1(self):
            win=Toplevel()
            menuPrincipal.Page1(win)
            self.window.withdraw()
            win.deiconify()

def page():
    window= Tk()
    MenuTransaccion(window)
    window.mainloop()

if __name__ == "__main__":
    page()