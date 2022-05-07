from tkinter import *
import os
import sys
from tkinter import messagebox
import cv2
import time
from pyzbar.pyzbar import decode
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, '..', 'DB' )
sys.path.append( controller_dir )
from dbController import DAO
dao=DAO()
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
used_codes=[]
class controller():
    #Funcion encargada de mostrar el frame requerido sin embargo, requiere que se carguen todos los frames mediante un for
    def framesManager(self,framesList,frametoShow):
        for frame in framesList:
            frame.grid(row=0,column=0,sticky="nsew")
        frametoShow.tkraise()

    def retiro():
        #>10000 y digitos en 5 5
        pass

    def getCardInfo(self):
        camera=True

        while camera:
                success,frame=cap.read()
                for code in decode(frame):
                    if code.data.decode('utf-8') not in used_codes:
                        cardInfo=code.data.decode('utf-8')
                        cardInfoList=cardInfo.split()
                        print(cardInfoList)
                        used_codes.append(code.data.decode('utf-8'))
                        time.sleep(5)
                        camera=False
                            #self.framesManager(framesList,frametoShow)
                    elif code.data.decode('utf-8') in used_codes:
                        messagebox.showerror(message="La camara ya esta activada",title="Error!")
                        time.sleep(5)
                    else:
                        pass
                cv2.imshow("Test",frame)
                cv2.waitKey(1)
        cap.release()
        cv2.destroyAllWindows()
        return cardInfoList

    def passwordValidation(self,cardInfoList,passwordGUI,framesList,frametoShow):
        accountId=int(cardInfoList[1])
        cards=dao.getTableInfo(3)
        passEntryTries=0
        for card in cards:
            if card[1]==accountId:
                codeExists=True
                break
        if codeExists:
            passwordScheme=dao.getInfo(accountId)
            passwordScheme=int(passwordScheme[0])
            if passwordScheme==int(passwordGUI):
                passEntryTries=0
                self.framesManager(framesList,frametoShow)
            else:
                messagebox.showerror(message="contraseña errada")
                passEntryTries+=1

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

    def validateR(self,entry,text,framesList,frametoShow):
        if int(text) < 2700000 and int(text) %5==0:
            entry.delete("0","end")
            self.framesManager(framesList,frametoShow)
        else:
            print("Su numero ingresado no es correcto intente de nuevo")


