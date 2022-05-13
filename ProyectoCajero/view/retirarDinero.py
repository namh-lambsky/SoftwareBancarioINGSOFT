from tkinter import *
from PIL import Image, ImageTk
import ingresoSinTarjeta,ingresoConTarjeta


class MenuRetirarDinero:
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
        fondoMenuRetirarDinero= Image.open("VIEW/imagenes/RetirarDinero.png")
        resizeImagef=fondoMenuRetirarDinero.resize((1250,580))
        fondoMenuRetirarDinero= ImageTk.PhotoImage(resizeImagef)

        #MenuRetirarDinero--------------------------------------------------------------------------

        menuRetirarDinerofondo=Label(self.window, image=fondoMenuRetirarDinero)
        menuRetirarDinerofondo.image=fondoMenuRetirarDinero
        menuRetirarDinerofondo.place(x=0,y=0)

        #botones MenuRetirarDinero

        menuTransaccionBtRetirarDinero10000= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDinero10000.place(x=25,y=10)

        menuTransaccionBtRetirarDinero20000= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDinero20000.place(x=25,y=145)

        menuTransaccionBtRetirarDinero50000= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDinero50000.place(x=25,y=280)

        menuTransaccionBtRetirarDineroFinalizar= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDineroFinalizar.place(x=25,y=415)

        menuTransaccionBtRetirarDinero150000= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDinero150000.place(x=1170,y=10)

        menuTransaccionBtRetirarDinero250000= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDinero250000.place(x=1170,y=145)

        menuTransaccionBtRetirarDinero350000= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDinero350000.place(x=1170,y=280)

        menuTransaccionBtRetirarDineroOtroValor= Button(self.window, padx=25, pady=15,border=0, bg="#DD5222")
        menuTransaccionBtRetirarDineroOtroValor.place(x=1170,y=415)
        

        




def page():
    window= Tk()
    MenuRetirarDinero(window)
    window.mainloop()

if __name__ == "__main__":
    page()




