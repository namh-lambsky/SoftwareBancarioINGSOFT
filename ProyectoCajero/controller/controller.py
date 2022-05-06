from tkinter import *
import os
import sys
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, '..', 'DB' )
sys.path.append( controller_dir )
from dbController import DAO
dao=DAO()

class controller():
    #Funcion encargada de mostrar el frame requerido sin embargo, requiere que se carguen todos los frames mediante un for

    def framesManager(self,framesList,frametoShow):
        for frame in framesList:
            frame.grid(row=0,column=0,sticky="nsew")
        frametoShow.tkraise()

    def getCardInfo():
        pass

    def entryPasswordValidation(self,entry,framesList,frametoShow):
        try:
            passwordEntry=entry.get()
            passwordIsCorrect=True
            print(passwordEntry)
            pass
            if passwordIsCorrect:
                self.framesManager(framesList,frametoShow)
                entry.delete("0","end")
        except Exception as e:
            print ("error: "+str(e))

    def clearTextInput(self,entry,framesList,frametoShow):
        entry.delete("0","end")
        self.framesManager(framesList,frametoShow)
