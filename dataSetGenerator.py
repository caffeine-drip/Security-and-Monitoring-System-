import cv2
import sqlite3

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('Classifiers/face.xml')
i=0
offset=50

def insertOrUpdate(Id,name,Rno,year,sec):
    conn=sqlite3.connect("DB/datab2.db")
    cmd="SELECT * FROM fulldb WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    ifRecordExist=0
    for row in cursor:
        ifRecordExist=1
        
    if(ifRecordExist==1):
        print"as"
        cmd= "UPDATE fulldb SET Name="+str(name)+",RollNo="+str(Rno)+",Year="+str(year)+",Section="+str(sec)+" WHERE ID="+str(Id)
    else:
        print"as2"
        cmd="INSERT INTO fulldb(ID,Name,RollNo,Year,Section) Values("+str(Id)+","+str(name)+","+str(Rno)+","+str(year)+","+str(sec)+")"
        
    conn.execute(cmd)
    conn.commit()
    conn.close()
    
Id=raw_input("enter ID ")
n=Id
Id="'"+Id+"'"
name=raw_input("enter your Name ")
name="'"+name+"'"
Rno=raw_input("enter your Rno ,if not applicable leave empty ")
Rno="'"+Rno+"'"
year=raw_input("enter your Year ,if not applicable leave empty ")
year="'"+year+"'"
sec=raw_input("enter your Section ,if not applicable leave empty ")
sec="'"+sec+"'"

insertOrUpdate(Id,name,Rno,year,sec)

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("dataSet/ID-"+str(n)+'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow('Faces',im[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.waitKey(100)
    if i>120:
        cam.release()
        cv2.destroyAllWindows()
        break

