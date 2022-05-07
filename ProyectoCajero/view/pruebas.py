import cv2
import time
import os
import sys
script_dir = os.path.dirname( __file__ )
controller_dir = os.path.join( script_dir, '..', 'DB' )
sys.path.append( controller_dir )
from dbController import DAO
from pyzbar.pyzbar import decode
dao=DAO()
"""cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
camera=True
used_codes=[]

def getCardInfo():
    while camera:
        success,frame=cap.read()
        for code in decode(frame):
            if code.data.decode('utf-8') not in used_codes:
                a=code.data.decode('utf-8')
                print(a.split())
                used_codes.append(code.data.decode('utf-8'))
                time.sleep(5)
            elif code.data.decode('utf-8') in used_codes:
                print("no")
                time.sleep(5)
            else:
                pass
        cv2.imshow("Test",frame)
        cv2.waitKey(1)"""


a=dao.getInfo(101010101)
print(int(a[0]))
