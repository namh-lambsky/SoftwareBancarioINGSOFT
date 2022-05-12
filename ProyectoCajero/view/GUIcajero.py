from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font

root = Tk()
root.title("Cajero Automatico Bancolombia")
#root.iconbitmap('imagenes/LogoBancolombia.ico')
root.geometry("1250x580")
root.resizable(False,False)

#Fondos de la pagina principal
bgPrincipal= Image.open("imagenes/Pantallaprincipal.png")
resizeImagef=bgPrincipal.resize((1250,580))
bgPrincipal= ImageTk.PhotoImage(resizeImagef)

fondoingresarTarjeta= Image.open("VIEW/imagenes/2.png")
resizeImagef=fondoingresarTarjeta.resize((1250,580))
fondoingresarTarjeta= ImageTk.PhotoImage(resizeImagef)




my_canvas= Canvas(root, width=1250, height= 580)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bgPrincipal, anchor="nw")

#fuente de letra personalizada
fuenteLetra= Font(
    family="Helvetica",
    size=20,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0
)
#Se crean los botones y los textos de la pagina de ingreso
MenuPrincipalBtIngresarTarjeta= Button(root, padx=25,border=0, pady=15, bg="#DD5222",command=LoadIngresoContraseñaContent())
MenuPrincipalBtIngresarSinTarjeta= Button(root, padx=25,border=0, pady=15, bg="#DD5222")
LbMenuP= Label(root, text="INGRESE TARJETA", font=fuenteLetra,bg="white")
LbMenuS= Label(root, text="INGRESE SIN TARJETA", font=fuenteLetra,bg="white")

#Se crean los botones y los textos de la pagina de ingreso contraseña
ingresarTarjetaBtIngresar= Button(root, padx=25,border=0, pady=15, bg="#7ed957" )
ingresarTarjetaBt2Ingresar= Button(root, padx=25,border=0, pady=15, bg="#e61717" )
LbIngresarC= Label(root, text="INGRESAR", font=fuenteLetra, bg="white")
LbFinalizarC= Label(root, text="FINALIZAR", font=fuenteLetra,bg="white")


#Funcion creada para cargar la pagina de ingreso
def LoadMainMenuContent():
    #Se cargan los botones y los textos de la pagina de ingreso
    MenuPrincipalBtIngresarSinTarjeta.place(relx=0.92,rely=0.74)
    MenuPrincipalBtIngresarTarjeta.place(relx=0.020,rely=0.74)
    LbMenuP.place(relx=0.08,rely=0.75)
    LbMenuS.place(relx=0.65,rely=0.75)

def DeleteMainMenuContent():
    MenuPrincipalBtIngresarTarjeta.destroy()
    LbMenuP.destroy()
    MenuPrincipalBtIngresarSinTarjeta.destroy()
    LbMenuS.destroy()

def DeleteIngresoContraseñaContent():
    ingresarTarjetaBtIngresar.destroy()
    ingresarTarjetaBt2Ingresar.destroy()
    LbIngresarC.destroy()
    LbFinalizarC.destroy()

def LoadIngresoContraseñaContent():
    
    ingresarTarjetaBtIngresar.place(relx=0.92,rely=0.74)
    ingresarTarjetaBt2Ingresar.place(relx=0.020,rely=0.74)
    LbIngresarC.place(relx=0.08,rely=0.75)
    LbFinalizarC.place(relx=0.65,rely=0.75)










root.mainloop()