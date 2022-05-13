from tkinter import *
from PIL import Image, ImageTk
from argparse import ZERO_OR_MORE
from ctypes import resize
from platform import win32_edition
import menuPrincipal, ingresoTarjetaContraseña


class Page2:
    def __init__(self,window):
        self.window= window
        self.window.geometry("1250x580")
        self.window.resizable(0,0)
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        #self.window.state("zoomed")
        #ingresarTarjeta---------------------------------------------------------
        fondoingresarTarjeta= Image.open("view/imagenes/IngreseCodigoTarjeta.png")
        resizeImagef=fondoingresarTarjeta.resize((1250,580))
        fondoingresarTarjeta= ImageTk.PhotoImage(resizeImagef)

        #iconos
        contraseñaIcon= Image.open("VIEW/imagenes/4.png")
        resizeImageC=contraseñaIcon.resize((300,50))
        contraseñaIcon=ImageTk.PhotoImage(resizeImageC)

        #ingresarTarjeta---------------------------------------------------------
        ingresarTarjetafondo=Label(self.window, image=fondoingresarTarjeta)
        ingresarTarjetafondo.image=fondoingresarTarjeta
        ingresarTarjetafondo.place(x=0,y=0)

        ingresoTarjetaLb=Label(self.window,image=contraseñaIcon,border=0)
        ingresoTarjetaLb.image=contraseñaIcon
        ingresoTarjetaLb.place(x=510,y=200)

        #Comando para la validación del entry(que sean 4 digitos y que sean numeros)
        def validate_entry(text, new_text):
        # Primero chequear que el contenido total no exceda los diez caracteres.
            if len(new_text) > 10:
                return False
        # Luego, si la validación anterior no falló, chequear que el texto solo
        # contenga números.
            return text.isdecimal()

        #Comando para eliminar espacio de texto
        #Entry para el ingreso de la contraseña
        ingresoTarjetaTx = Entry(self.window, show="*",width=6,font=("Helvetica",24),border=0)
        ingresoTarjetaTx.place(x=630,y=204)
        ingresoTarjetaTx.focus_set()
        ingresoTarjetaTx.config(validate='key',validatecommand=(self.window.register(validate_entry), "%S", "%P"))

        #botones ingresarTarjeta
        ingresarTarjetaBtIngresar= Button(self.window, padx=25,border=0, pady=15, bg="#7ed957", command=self.go_page3)
        ingresarTarjetaBtIngresar.place(x=100,y=345)

        ingresarTarjetaBt2Ingresar= Button(self.window, padx=25,border=0, pady=15, bg="#e61717", command=self.go_page1)
        ingresarTarjetaBt2Ingresar.place(x=100,y=445)


    def go_page3(self):
        win=Toplevel()
        ingresoTarjetaContraseña.Page3(win)
        self.window.withdraw()
        win.deiconify()

    def go_page1(self):
        win=Toplevel()
        menuPrincipal.Page1(win)
        self.window.withdraw()
        win.deiconify()


def page():
    window= Tk()
    Page2(window)
    window.mainloop()



if __name__ == "__main__":
    page()