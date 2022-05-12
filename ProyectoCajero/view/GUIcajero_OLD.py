from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os
import sys
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, '..', 'controller' )
sys.path.append( controller_dir )
from controller import controller

c=controller()
ventana=Tk()
ventana.geometry("1250x580")
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)
ventana.resizable (0,0)

#Numero de paginas

MenuPrincipal= Frame(ventana)
ingresarTarjeta= Frame(ventana)
ingresarSinTarjeta= Frame(ventana)
MenuTransaccion= Frame(ventana)
IngresoTarjetaContraseña= Frame(ventana)
retirarDinero= Frame(ventana)
consultarSaldo= Frame(ventana)
transferencias= Frame(ventana)
transferenciasOp= Frame(ventana)
transferenciaNumeroDeCuenta= Frame(ventana)
ConfirmaciónCuenta= Frame(ventana)
CodigoDeBarras= Frame(ventana)
ImprimirRecibo= Frame(ventana)
NuevoSaldo= Frame(ventana)

framesList=[MenuPrincipal, ingresarTarjeta,ingresarSinTarjeta, IngresoTarjetaContraseña,MenuTransaccion, retirarDinero, consultarSaldo, transferencias, transferenciasOp, transferenciaNumeroDeCuenta, ConfirmaciónCuenta, CodigoDeBarras, ImprimirRecibo, NuevoSaldo]

c.framesManager(framesList,MenuPrincipal)


#imagenes
fondo= Image.open("VIEW/imagenes/Pantallaprincipal.png")
resizeImagef=fondo.resize((1250,580))
fondo= ImageTk.PhotoImage(resizeImagef)

fondoingresarTarjeta= Image.open("VIEW/imagenes/2.png")
resizeImagef=fondoingresarTarjeta.resize((1250,580))
fondoingresarTarjeta= ImageTk.PhotoImage(resizeImagef)

fondoIngresarSinTarjeta= Image.open("VIEW/imagenes/3.png")
resizeImagef=fondoIngresarSinTarjeta.resize((1250,580))
fondoIngresarSinTarjeta= ImageTk.PhotoImage(resizeImagef)

fondoMenuTransaccion= Image.open("VIEW/imagenes/MenuTransaccion.png")
resizeImagef=fondoMenuTransaccion.resize((1250,580))
fondoMenuTransaccion= ImageTk.PhotoImage(resizeImagef)

fondoIngresoTarjetaContraseña= Image.open("VIEW/imagenes/IngresoTarjetaContraseña.png")
resizeImagef=fondoIngresoTarjetaContraseña.resize((1250,580))
fondoIngresoTarjetaContraseña= ImageTk.PhotoImage(resizeImagef)

fondoRetirarDinero= Image.open("VIEW/imagenes/RetirarDinero.png")
resizeImagef=fondoRetirarDinero.resize((1250,580))
fondoRetirarDinero= ImageTk.PhotoImage(resizeImagef)

fondoConsultarSaldo= Image.open("VIEW/imagenes/ConsultarSaldo.png")
resizeImagef=fondoConsultarSaldo.resize((1250,580))
fondoConsultarSaldo= ImageTk.PhotoImage(resizeImagef)

fondoTransferencias= Image.open("VIEW/imagenes/Transferencias.png")
resizeImagef=fondoTransferencias.resize((1250,580))
fondoTransferencias= ImageTk.PhotoImage(resizeImagef)

fondoTransferenciasOp= Image.open("VIEW/imagenes/TransferenciasOp.png")
resizeImagef=fondoTransferenciasOp.resize((1250,580))
fondoTransferenciasOp= ImageTk.PhotoImage(resizeImagef)

fondoTransferenciaNumeroDeCuenta= Image.open("VIEW/imagenes/TransferenciaNumeroDeCuenta.png")
resizeImagef=fondoTransferenciaNumeroDeCuenta.resize((1250,580))
fondoTransferenciaNumeroDeCuenta= ImageTk.PhotoImage(resizeImagef)

fondoConfirmacionCuenta= Image.open("VIEW/imagenes/ConfirmacionCuenta.png")
resizeImagef=fondoConfirmacionCuenta.resize((1250,580))
fondoConfirmacionCuenta= ImageTk.PhotoImage(resizeImagef)

fondoCodigoDeBarras= Image.open("VIEW/imagenes/CodigoDeBarras.png")
resizeImagef=fondoCodigoDeBarras.resize((1250,580))
fondoCodigoDeBarras= ImageTk.PhotoImage(resizeImagef)

fondoImprimirRecibo= Image.open("VIEW/imagenes/ImprimirRecibo.png")
resizeImagef=fondoImprimirRecibo.resize((1250,580))
fondoImprimirRecibo= ImageTk.PhotoImage(resizeImagef)

fondoNuevoSaldo= Image.open("VIEW/imagenes/NuevoSaldo.png")
resizeImagef=fondoNuevoSaldo.resize((1250,580))
fondoNuevoSaldo= ImageTk.PhotoImage(resizeImagef)


#iconos
contraseñaIcon= Image.open("VIEW/imagenes/4.png")
resizeImageC=contraseñaIcon.resize((300,50))
contraseñaIcon=ImageTk.PhotoImage(resizeImageC)



#MenuPrincipal---------------------------------------------------------
#dataList=c.getCardInfo()
#label
MenuPrincipalFondo =Label(MenuPrincipal, image=fondo)
MenuPrincipalFondo.place(x=0,y=0)


#botones
MenuPrincipalBtIngresarTarjeta= Button(MenuPrincipal, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,IngresoTarjetaContraseña))
MenuPrincipalBtIngresarTarjeta.place(x=15,y=435)

MenuPrincipalBtIngresarSinTarjeta= Button(MenuPrincipal, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,ingresarSinTarjeta))
MenuPrincipalBtIngresarSinTarjeta.place(x=1175,y=435)

#MenuingresarTarjeta---------------------------------------------------------
ingresarTarjetafondo=Label(ingresarTarjeta, image=fondoingresarTarjeta)
ingresarTarjetafondo.place(x=0,y=0)

#botones ingresarTarjeta
ingresarTarjetaBtIngresar= Button(ingresarTarjeta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.getCardInfo(framesList,IngresoTarjetaContraseña))
ingresarTarjetaBtIngresar.place(x=100,y=345)



ingresarTarjetaBt2Ingresar= Button(ingresarTarjeta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuPrincipal))
ingresarTarjetaBt2Ingresar.place(x=100,y=445)

#IngresoTarjetaContraseña---------------------------------------------------------------------------------

IngresoTarjetaContraseñafondo=Label(IngresoTarjetaContraseña, image=fondoIngresoTarjetaContraseña)
IngresoTarjetaContraseñafondo.place(x=0,y=0)

IngresoTarjetaContraseñaLb=Label(IngresoTarjetaContraseña,image=contraseñaIcon,border=0)
IngresoTarjetaContraseñaLb.place(x=510,y=200)

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
IngresoTarjetaContraseñaTx = Entry(IngresoTarjetaContraseña, show="*",width=6,font=("Helvetica",24),border=0)
IngresoTarjetaContraseñaTx.place(x=630,y=204)
IngresoTarjetaContraseñaTx.focus_set()
IngresoTarjetaContraseñaTx.config(validate='key',validatecommand=(ventana.register(validate_entry), "%S", "%P"))

#botones IngresoTarjeta
IngresoTarjetaBtIngresar= Button(IngresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.passwordValidation(c.getCardInfo(),IngresoTarjetaContraseñaTx.get(),framesList,MenuTransaccion))
IngresoTarjetaBtIngresar.place(x=100,y=345)

IngresoTarjetaBtFinalizar= Button(IngresoTarjetaContraseña, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(IngresoTarjetaContraseñaTx,framesList,MenuPrincipal))
IngresoTarjetaBtFinalizar.place(x=100,y=445)

#ingresarSinTarjeta----------------------------------------------------------------

ingresarSinTarjetafondo=Label(ingresarSinTarjeta, image=fondoIngresarSinTarjeta)
ingresarSinTarjetafondo.place(x=0,y=0)

IngresoSinTarjetaContraseñaLb=Label(ingresarSinTarjeta,image=contraseñaIcon,border=0)
IngresoSinTarjetaContraseñaLb.place(x=510,y=210)

IngresoSinTarjetaContraseñaTx= Entry(ingresarSinTarjeta, show="*",width=10,font=("Helvetica",24),border=0)
IngresoSinTarjetaContraseñaTx.place(x=557,y=214)

#BotonesingresarSinTarjeta

ingresarSinTarjetaBtIngresar= Button(ingresarSinTarjeta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.clearTextInput(IngresoSinTarjetaContraseñaTx,framesList,MenuTransaccion))
ingresarSinTarjetaBtIngresar.place(x=100,y=345)

ingresarSinTarjetaBt2Ingresar= Button(ingresarSinTarjeta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(IngresoSinTarjetaContraseñaTx,framesList,MenuPrincipal))
ingresarSinTarjetaBt2Ingresar.place(x=100,y=445)

#MenuTransaccion--------------------------------------------------------------------------

MenuTransaccionfondo=Label(MenuTransaccion, image=fondoMenuTransaccion)
MenuTransaccionfondo.place(x=0,y=0)

#botones MenuTransaccion
MenuTransaccionBtIngresar= Button(MenuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: c.framesManager(framesList,retirarDinero))
MenuTransaccionBtIngresar.place(x=25,y=160)

MenuTransaccion2BtIngresar= Button(MenuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: c.framesManager(framesList,consultarSaldo))
MenuTransaccion2BtIngresar.place(x=25,y=295)

MenuTransaccion3BtIngresar= Button(MenuTransaccion, padx=25, pady=15,border=0, bg="#DD5222",command = lambda: c.framesManager(framesList,transferencias))
MenuTransaccion3BtIngresar.place(x=1170,y=160)

#Retirar Dinero-----------------------------------------------------------------------------------------------
RetirarDinerofondo=Label(retirarDinero, image=fondoRetirarDinero)
RetirarDinerofondo.place(x=0,y=0)

RetirarDineroLb=Label(retirarDinero,image=contraseñaIcon,border=0)
RetirarDineroLb.place(x=510,y=200)

#Comando de validacion

def validate_entryR(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 7:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()





#Comando para la validación del entry(que sean >10000 digitos y que sean numeros)
def validate_entryRetiro(text):
    if int(text) < 2700000 and int(text) %5==0:
        return True
    else:
        print("Su numero ingresado no es correcto intente de nuevo")
#entry

RetirarDineroTx= Entry(retirarDinero,width=10,font=("Helvetica",24),border=0)
RetirarDineroTx.place(x=557,y=204)
RetirarDineroTx.focus_set()
RetirarDineroTx.config(validate='key',validatecommand=(ventana.register(validate_entryR), "%S", "%P"))


#botones RetirarDinero

RetirarDineroBtIngresar= Button(retirarDinero, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.validateR(RetirarDineroTx,RetirarDineroTx.get(),framesList,consultarSaldo))
RetirarDineroBtIngresar.place(x=100,y=345)

RetirarDineroBt2Ingresar= Button(retirarDinero, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(RetirarDineroTx,framesList,MenuTransaccion))
RetirarDineroBt2Ingresar.place(x=100,y=445)

#Consultar saldo-------------------------------------------------------------------------------------------------

#label
ConsultarSaldoFondo =Label(consultarSaldo, image=fondoConsultarSaldo)
ConsultarSaldoFondo.place(x=0,y=0)


#botones
ConsultarSaldoBtImprimir= Button(consultarSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,ImprimirRecibo))
ConsultarSaldoBtImprimir.place(x=15,y=290)

ConsultarSaldoBtVer= Button(consultarSaldo, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,NuevoSaldo))
ConsultarSaldoBtVer.place(x=1175,y=290)


#transferencias-----------------------------------------------------------------------------------------------------

#label
transferenciasFondo =Label(transferencias, image=fondoTransferencias)
transferenciasFondo.place(x=0,y=0)


#botones 
transferenciasBtAhorro= Button(transferencias, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,transferenciasOp))
transferenciasBtAhorro.place(x=15,y=270)

transferenciasBtCorriente= Button(transferencias, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,transferenciasOp))
transferenciasBtCorriente.place(x=1175,y=270)

#TransferenciasOp----------------------------------------------------------------------------------------------------

#label
transferenciasOpFondo =Label(transferenciasOp, image=fondoTransferenciasOp)
transferenciasOpFondo.place(x=0,y=0)


#botones
transferenciasOpBtNumero= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,transferenciaNumeroDeCuenta))
transferenciasOpBtNumero.place(x=15,y=270)

transferenciasOpBtCodigo= Button(transferenciasOp, padx=25,border=0, pady=15, bg="#DD5222",command = lambda: c.framesManager(framesList,CodigoDeBarras))
transferenciasOpBtCodigo.place(x=1175,y=270)

#transferenciaNumeroDeCuenta--------------------------------------------------------------------------------------------

transferenciaNumeroDeCuentafondo=Label(transferenciaNumeroDeCuenta, image=fondoTransferenciaNumeroDeCuenta)
transferenciaNumeroDeCuentafondo.place(x=0,y=0)

transferenciaNumeroDeCuentafondoLb=Label(transferenciaNumeroDeCuenta,image=contraseñaIcon,border=0)
transferenciaNumeroDeCuentafondoLb.place(x=510,y=200)

#




#Verificacion

def validate_entryN(text, new_text):
    # Primero chequear que el contenido total no exceda los diez caracteres.
    if len(new_text) > 10:
        return False
    # Luego, si la validación anterior no falló, chequear que el texto solo
    # contenga números.
    return text.isdecimal()


transferenciaNumeroDeCuentaTx= Entry(transferenciaNumeroDeCuenta,width=10,font=("Helvetica",24),border=0)
transferenciaNumeroDeCuentaTx.place(x=557,y=204)
transferenciaNumeroDeCuentaTx.focus_set()
transferenciaNumeroDeCuentaTx.config(validate='key',validatecommand=(ventana.register(validate_entryN), "%S", "%P"))

#botones transferenciaNumeroDeCuenta

transferenciaNumeroDeCuentaBtIngresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.clearTextInput(transferenciaNumeroDeCuentaTx,framesList,ConfirmaciónCuenta))
transferenciaNumeroDeCuentaBtIngresar.place(x=100,y=345)

transferenciaNumeroDeCuentaBt2Ingresar= Button(transferenciaNumeroDeCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.clearTextInput(transferenciaNumeroDeCuentaTx,framesList,MenuTransaccion))
transferenciaNumeroDeCuentaBt2Ingresar.place(x=100,y=445)

#ConfirmaciónCuenta-------------------------------------------------------------------------------------------------------

#label
ConfirmaciónCuentaFondo =Label(ConfirmaciónCuenta, image=fondoConfirmacionCuenta)
ConfirmaciónCuentaFondo.place(x=0,y=0)


#botones
ConfirmaciónCuentaBtIngresar= Button(ConfirmaciónCuenta, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.framesManager(framesList,consultarSaldo))
ConfirmaciónCuentaBtIngresar.place(x=100,y=345)

ConfirmaciónCuentaBt2Ingresar= Button(ConfirmaciónCuenta, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuTransaccion))
ConfirmaciónCuentaBt2Ingresar.place(x=100,y=445)

#CodigoDeBarras-------------------------------------------------------------------------------------------------------------

CodigoDeBarrasfondo=Label(CodigoDeBarras, image=fondoCodigoDeBarras)
CodigoDeBarrasfondo.place(x=0,y=0)


#Botones

CodigoDeBarrasBtIngresar= Button(CodigoDeBarras, padx=25,border=0, pady=15, bg="#7ed957",command = lambda: c.framesManager(framesList,ConfirmaciónCuenta))
CodigoDeBarrasBtIngresar.place(x=100,y=345)

CodigoDeBarrasBt2Ingresar= Button(CodigoDeBarras, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuTransaccion))
CodigoDeBarrasBt2Ingresar.place(x=100,y=445)

#ImprimirRecibo------------------------------------------------------------------------------------------------------------------------

ImprimirRecibofondo=Label(ImprimirRecibo, image=fondoImprimirRecibo)
ImprimirRecibofondo.place(x=0,y=0)


#Botones

ImprimirReciboBtIngresar= Button(ImprimirRecibo, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuPrincipal))
ImprimirReciboBtIngresar.place(x=100,y=345)

#NuevoSaldo-----------------------------------------------------------------------------------------------------------------------------

NuevoSaldofondo=Label(NuevoSaldo, image=fondoNuevoSaldo)
NuevoSaldofondo.place(x=0,y=0)

#Botones

NuevoSaldoBtIngresar= Button(NuevoSaldo, padx=25,border=0, pady=15, bg="#e61717",command = lambda: c.framesManager(framesList,MenuPrincipal))
NuevoSaldoBtIngresar.place(x=100,y=345)


    





ventana.mainloop()
