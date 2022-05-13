from tkinter import *
from PIL import Image, ImageTk
import menuPrincipal,menuTransaccion
import os
import sys
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, '..', 'controller' )
sys.path.append( controller_dir )
from controller import controller

c=controller()
class Page4:
    def __init__(self,window):
            self.window= window
            self.window.geometry("1250x580")
            self.window.resizable(0,0)
            self.window.rowconfigure(0,weight=1)
            self.window.columnconfigure(0,weight=1)

            ingresoSinContraseñaFondo= Image.open("view/imagenes/IngresoTarjetaContraseña.png")
            resizeImagef=ingresoSinContraseñaFondo.resize((1250,580))
            ingresoSinContraseñaFondo= ImageTk.PhotoImage(resizeImagef)

            MenuPrincipalFondoLb= Label(self.window, image=ingresoSinContraseñaFondo)
            MenuPrincipalFondoLb.image=ingresoSinContraseñaFondo
            MenuPrincipalFondoLb.place(x=0,y=0)

            #Comando para la validación del entry(que sean 4 digitos y que sean numeros)
            def validate_entry(text, new_text):
            # Primero chequear que el contenido total no exceda los diez caracteres.
                if len(new_text) > 4:
                    return False
            # Luego, si la validación anterior no falló, chequear que el texto solo
            # contenga números.
                return text.isdecimal()

            #Comando para eliminar espacio de texto
            #Entry para el ingreso de la contraseña
            ingresoTarjetaContraseñaTx = Entry(self.window, show="*",width=6,font=("Helvetica",24),border=0)
            ingresoTarjetaContraseñaTx.place(x=630,y=204)
            ingresoTarjetaContraseñaTx.focus_set()
            ingresoTarjetaContraseñaTx.config(validate='key',validatecommand=(self.window.register(validate_entry), "%S", "%P"))

            #botones IngresoTarjeta
            ingresoTarjetaBtIngresar= Button(self.window, padx=25,border=0, pady=15, bg="#7ed957",command=lambda:login(cardInfo,ingresoTarjetaContraseñaTx))
            ingresoTarjetaBtIngresar.place(x=100,y=345)

            ingresoTarjetaBtFinalizar= Button(self.window, padx=25,border=0, pady=15, bg="#e61717",command=go_page1)
            ingresoTarjetaBtFinalizar.place(x=100,y=445)

            cardInfo=c.getCardList()

            def login(cardInfoList,ingresoTarjetaContraseñaTx):
                if c.passwordValidation(cardInfoList,ingresoTarjetaContraseñaTx.get()):
                    go_MenuTransacciones()


            def go_MenuTransacciones(self):
                win=Toplevel()
                menuTransaccion.MenuTransaccion(win)
                self.window.withdraw()
                win.deiconify()

            def go_page1(self):
                win=Toplevel()
                menuPrincipal.Page1(win)
                self.window.withdraw()
                win.deiconify()

def page():
    window= Tk()
    Page4(window)
    window.mainloop()

if __name__ == "__main__":
    page()




