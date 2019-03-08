import cv2,os
import numpy as np
from PIL import Image 
import pickle
import sqlite3

conn=sqlite3.connect("DB/datab2.db")
cmd="DROP TABLE IF EXISTS PresentInSec4B"
cursor=conn.execute(cmd)
conn.commit()
conn.close()

conn=sqlite3.connect("DB/datab2.db")
cmd="CREATE TABLE IF NOT EXISTS PresentInSec4B(Name string,RollNo int PRIMARY KEY)"
cursor=conn.execute(cmd)
conn.commit()
conn.close()


recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

def getData(Id):
    conn=sqlite3.connect("DB/datab2.db")
    cmd="SELECT * FROM fulldb WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    user=None
    for row in cursor:
        user=row
    conn.close()
    return user

def sendData(User):
    sec=User[4]
    Rno=str(User[2])
    Rno="'"+Rno+"'"
    name=User[1]
    name="'"+name+"'"
    year=User[3]
    if(sec!="b" and sec !="B"):
        return
    conn=sqlite3.connect("DB/datab2.db")
    cmd="SELECT * FROM PresentInSec4B WHERE RollNo="+str(Rno)
    cursor=conn.execute(cmd)
    ifRecordExist=0
    for row in cursor:
        ifRecordExist=1
        
    if(ifRecordExist!=1):
        cmd="INSERT INTO PresentInSec4B(Name,RollNo) Values("+str(name)+","+str(Rno)+")"
        conn.execute(cmd)
        #print"inInsert"
    #else:
        #cmd= "UPDATE PresentInSec4A SET Name="+str(name)+" WHERE ID="+str(Rno)
        
    conn.commit()
    conn.close()



cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) 
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#im = cv2.imread('ex.jpg')
#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        print Idd ,conf
        if conf<=70:
            user=getData(Id)
            if(user != None):     
                cv2.cv.PutText(cv2.cv.fromarray(im),str(user[1]), (x,y+h),font, 255) 
                sendData(user)
        cv2.imshow('Detector',im)
        cv2.waitKey(30)










