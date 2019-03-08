from Tkinter import *
import os
import threading 
import time



def b():
    def callback():
        os.system("python dataSetGenerator.py")
    w1=threading.Thread( name='my_servic2e',target=callback)
    w1.start()

def c():
    def callback1():
        os.system("python Trainer.py")
    w2=threading.Thread( name='my_servic3e',target=callback1)
    w2.start()

def d():
    def callback2():
        os.system("python detectorForA.py")
    w3=threading.Thread( name='my_servic4e',target=callback2)
    w3.start()

def e():
    def callback2():
        os.system("python detectorForB.py")
    w3=threading.Thread( name='my_servic5e',target=callback2)
    w3.start()

def f():
    def callback2():
        os.system("python detectorForHall.py")
    w3=threading.Thread( name='my_servic5e',target=callback2)
    w3.start()

def g():
    def callback2():
        os.system("python DatabCSV.py")
    w3=threading.Thread( name='my_servic6e',target=callback2)
    w3.start()

def h():
    def callback2():
        os.system("python AllCameraCSV.py")
    w3=threading.Thread( name='my_servic7e',target=callback2)
    w3.start()

    
master = Tk()
master.minsize(306, 300)
master.title("Attendence System")

nE=Label(master,text=("---------------------------------------------------------------------"))
nE.pack()
n=Label(master,text=" Ж Ж Ж Ж Ж |  The Main Attendence System Wnidow  | Ж Ж Ж Ж Ж ")
n.pack()
n1=Label(master,text=" Ж Ж Ж Ж Ж |         Various Modules Available         | Ж Ж Ж Ж Ж ")
n1.pack()
nE=Label(master,text=("---------------------------------------------------------------------"))
nE.pack()

n2=Label(master,text="___________________________________________")
n2.pack()
n2=Label(master,text="Modules")
n2.pack()
n2=Label(master,text="___________________________________________")
n2.pack()
n2=Label(master,text="")
n2.pack()

bE=Label(master,text=("To Generate Data Set"))
bE.pack()
b0 = Button(master, text="Data Set",command= b)
b0.pack()
n2=Label(master,text="")
n2.pack()

b1E=Label(master,text=("To Train Data Set"))
b1E.pack()
b1 = Button(master, text="Train Data Set", command=c)
b1.pack()
n2=Label(master,text="")
n2.pack()

b4E=Label(master,text=("Generate CSV for full Database"))
b4E.pack()
b4 = Button(master, text="Generate", command=g)
b4.pack()
n2=Label(master,text="")
n2.pack()

b4E=Label(master,text=("To Run Detection For Sec-A"))
b4E.pack()
b4 = Button(master, text="Run Detection", command=d)
b4.pack()
n2=Label(master,text="")
n2.pack()

b4E=Label(master,text=("To Run Detection For Sec-B"))
b4E.pack()
b4 = Button(master, text="Run Detection", command=e)
b4.pack()
n2=Label(master,text="")
n2.pack()

b4E=Label(master,text=("To Run Detection For Hall"))
b4E.pack()
b4 = Button(master, text="Run Detection", command=f)
b4.pack()
n2=Label(master,text="")
n2.pack()

b4E=Label(master,text=("To Track movement Of All Students"))
b4E.pack()
b4 = Button(master, text="Generate CSV of all Cameras", command=h)
b4.pack()
n2=Label(master,text="")
n2.pack()



    
mainloop()





