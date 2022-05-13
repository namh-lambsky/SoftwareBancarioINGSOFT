from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import os
import sys
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, '..', 'controller' )
sys.path.append( controller_dir )
#from controller import controller

root = Tk()
root.title("Cajero Automatico Bancolombia")
root.iconbitmap('view/imagenes/LogoBancolombia.ico')
root.geometry("1250x580")
root.resizable(False,False)

#Fondo de la pagina principal
bgPrincipal= Image.open("view/imagenes/Pantallaprincipal.png")
resizeImagef=bgPrincipal.resize((1250,580))
bgPrincipal= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina sin tarjeta
fondoIngresarSinTarjeta= Image.open("VIEW/imagenes/3.png")
resizeImagef=fondoIngresarSinTarjeta.resize((1250,580))
fondoIngresarSinTarjeta= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina menu transaccion
fondoMenuTransaccion= Image.open("VIEW/imagenes/MenuTransaccion.png")
resizeImagef=fondoMenuTransaccion.resize((1250,580))
fondoMenuTransaccion= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina de ingreso contraseña
fondoIngresoTarjetaContraseña= Image.open("VIEW/imagenes/IngresoTarjetaContraseña.png")
resizeImagef=fondoIngresoTarjetaContraseña.resize((1250,580))
fondoIngresoTarjetaContraseña= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Retiro de dinero
fondoRetirarDinero= Image.open("VIEW/imagenes/RetirarDinero.png")
resizeImagef=fondoRetirarDinero.resize((1250,580))
fondoRetirarDinero= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina consulta de saldo
fondoConsultarSaldo= Image.open("VIEW/imagenes/ConsultarSaldo.png")
resizeImagef=fondoConsultarSaldo.resize((1250,580))
fondoConsultarSaldo= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Transferencias
fondoTransferencias= Image.open("VIEW/imagenes/Transferencias.png")
resizeImagef=fondoTransferencias.resize((1250,580))
fondoTransferencias= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Transferencias (PENDIENTE USO)
fondoTransferenciasOp= Image.open("VIEW/imagenes/TransferenciasOp.png")
resizeImagef=fondoTransferenciasOp.resize((1250,580))
fondoTransferenciasOp= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Transferencias Ingreso de numero de cuenta
fondoTransferenciaNumeroDeCuenta= Image.open("VIEW/imagenes/TransferenciaNumeroDeCuenta.png")
resizeImagef=fondoTransferenciaNumeroDeCuenta.resize((1250,580))
fondoTransferenciaNumeroDeCuenta= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Transferencias-Confirmacion de numero de cuenta
fondoConfirmacionCuenta= Image.open("VIEW/imagenes/ConfirmacionCuenta.png")
resizeImagef=fondoConfirmacionCuenta.resize((1250,580))
fondoConfirmacionCuenta= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Transferencias-Lectura de codigo de barras
fondoCodigoDeBarras= Image.open("VIEW/imagenes/CodigoDeBarras.png")
resizeImagef=fondoCodigoDeBarras.resize((1250,580))
fondoCodigoDeBarras= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Transferencias Impresion de recibo
fondoImprimirRecibo= Image.open("VIEW/imagenes/ImprimirRecibo.png")
resizeImagef=fondoImprimirRecibo.resize((1250,580))
fondoImprimirRecibo= ImageTk.PhotoImage(resizeImagef)
#Fondo de la pagina Nuevo Saldo
fondoNuevoSaldo= Image.open("VIEW/imagenes/NuevoSaldo.png")
resizeImagef=fondoNuevoSaldo.resize((1250,580))
fondoNuevoSaldo= ImageTk.PhotoImage(resizeImagef)

#Campo
contraseñaIcon= Image.open("VIEW/imagenes/4.png")
resizeImageC=contraseñaIcon.resize((300,50))
contraseñaIcon=ImageTk.PhotoImage(resizeImageC)

#Se crean los botones y los textos de la pagina de ingreso
menuPrincipalFondo = Label(root, image=bgPrincipal)
menuPrincipalBtIngresarTarjeta = Button(root, padx=25,border=0, pady=15, bg="#DD5222",command=lambda:loadIngresoContraseñaContent())
menuPrincipalBtIngresarSinTarjeta = Button(root, padx=25,border=0, pady=15, bg="#DD5222")





#Se crean los botones y los textos de la pagina de transacciones
btRetiro=Button(root, padx=25,border=0, pady=15, bg="#DD5222")
btConsultaSaldo=Button(root, padx=25,border=0, pady=15, bg="#DD5222")
btTransferencias=Button(root, padx=25,border=0, pady=15, bg="#DD5222")


#Se cargan los botones y los textos de la pagina de ingreso
menuPrincipalBtIngresarSinTarjeta.place(relx=0.92,rely=0.74)
menuPrincipalBtIngresarTarjeta.place(relx=0.020,rely=0.74)
menuPrincipalFondo.place(x=0,y=0)

def loadMenuPrincipalContent(menuActual):
    if menuActual==1:
        deleteIngresoContraseñaContent()
    else:
        print("xd")
    menuPrincipalFondo = Label(root, image=bgPrincipal)
    menuPrincipalBtIngresarTarjeta = Button(root, padx=25,border=0, pady=15, bg="#DD5222",command=lambda:loadIngresoContraseñaContent())
    menuPrincipalBtIngresarSinTarjeta = Button(root, padx=25,border=0, pady=15, bg="#DD5222")
    menuPrincipalBtIngresarSinTarjeta.place(relx=0.92,rely=0.74)
    menuPrincipalBtIngresarTarjeta.place(relx=0.020,rely=0.74)
    menuPrincipalFondo.place(x=0,y=0)


def deleteMainMenuContent():
    menuPrincipalFondo.destroy()
    menuPrincipalBtIngresarTarjeta.destroy()
    menuPrincipalBtIngresarSinTarjeta.destroy()

def loadIngresoContraseñaContent():
    deleteMainMenuContent()

    #Se crean los botones y los textos de la pagina de ingreso contraseña
    ingresoTarjetaContraseñafondo=Label(root, image=fondoIngresoTarjetaContraseña)
    ingresoTarjetaContraseñaLb=Label(root,image=contraseñaIcon,border=0)
    ingresoTarjetaContraseñaTx = Entry(root, show="*",width=6,font=("Helvetica",24),border=0)
    ingresoTarjetaContraseñaTx.focus_set()

    ingresarTarjetaBtIngresar= Button(root, padx=25,border=0, pady=15, bg="#7ed957" )
    ingresarTarjetaBt2Ingresar= Button(root, padx=25,border=0, pady=15, bg="#e61717", command=lambda:loadMenuPrincipalContent(1))
    #Se Posicionan los botones
    ingresoTarjetaContraseñafondo.place(x=0,y=0)
    ingresoTarjetaContraseñaLb.place(x=510,y=200)
    ingresoTarjetaContraseñaTx.place(x=630,y=204)
    ingresarTarjetaBtIngresar.place(x=100,y=345)
    ingresarTarjetaBt2Ingresar.place(x=100,y=445)

def deleteIngresoContraseñaContent():
    ingresoTarjetaContraseñafondo.destroy()
    ingresoTarjetaContraseñaLb.destroy()
    ingresoTarjetaContraseñaTx.destroy()
    ingresarTarjetaBtIngresar.destroy()
    ingresarTarjetaBt2Ingresar.destroy()


def loadIngresarSinTarjetaContent():
    deleteMainMenuContent()

    #Se crean los botones y los textos de la pagina ingresar Sin Tarjeta

    ingresarSinTarjetafondo=Label(root, image=fondoIngresarSinTarjeta)
    ingresoSinTarjetaContraseñaLb=Label(root,image=contraseñaIcon,border=0)
    ingresoSinTarjetaContraseñaTx= Entry(root, show="*",width=10,font=("Helvetica",24),border=0)
    
    #Se Posicionan los botones
    ingresarSinTarjetafondo.place(x=0,y=0)
    ingresoSinTarjetaContraseñaLb.place(x=510,y=210)
    ingresoSinTarjetaContraseñaTx.place(x=557,y=214)




root.mainloop()
