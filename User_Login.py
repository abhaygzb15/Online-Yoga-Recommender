# USER MODULE REGISTER
import mysql.connector
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
def Register():
    def Clear():
        Txt1.delete("0",END)
        Txt2.delete("0",END)
        Txt3.delete("0",END)
        Txt4.delete("0",END)

    def Create(): 
      conn=mysql.connector.connect(host="localhost",user="root",
           password="tiger",database="project")
      cur=conn.cursor()
      print("*"*80)
      Name=Txt1.get()
      U_Name=Txt2.get()
      pwd=Txt3.get()
      dob=Txt4.get()
      query="INSERT INTO login VALUES ('{}','{}','{}','{}')".format(Name,U_Name,pwd,dob)
      cur.execute(query)
      cur.execute("commit")
      print("*"*80)
      W1.destroy()

    W1=Tk()
    W1.geometry("740x540")
    W1.configure(bg="#FFA500")
    W1.title("USERREGISTER SCREEN")
    image=Image.open("Medi.png")
    R=image.resize((460,250))
    R2=ImageTk.PhotoImage(R)
    Lb=Label(W1,image=R2)
    Lb.place(x=139,y=55)

    L1=Label(W1,text="  Y O G A     R I S I N G      A P P L I C A T I O N ",bg="light green",font=("TIMES NEW ROMAN",24,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0)

    F=Frame(W1,bg="purple",width=750,height=250,bd=20)
    F.place(x=10,y=340)
    L2=Label(W1,text="  ENTER THE REQUIRED DATA ",bg="light blue",font=("TIMES NEW ROMAN",25,"bold"))
    L2.place(x=114,y=320)

    Lb1=Label(F,text="TYPE YOUR NAME ,ex - Abc_us",relief=GROOVE,width=24)
    Lb1.place(x=0,y=20)
    Txt1=Entry(F,width=30)
    Txt1.place(x=250,y=20)

    Lb2=Label(F,text="TYPE YOUR USERNAME ,ex - Abc@info.in",relief=GROOVE,width=32)
    Lb2.place(x=0,y=50)
    Txt2=Entry(F,width=30)
    Txt2.place(x=250,y=50)

    Lb3=Label(F,text="TYPE YOUR PASSWORD (6-digit) ",relief=GROOVE,width=25)
    Lb3.place(x=0,y=80)
    Txt3=Entry(F,width=30,show="*")
    Txt3.place(x=250,y=80)

    Lb4=Label(F,text="TYPE YOUR DOB (YYYY-MM-DD) ",relief=GROOVE,width=25)
    Lb4.place(x=0,y=110)
    Txt4=Entry(F,width=30)
    Txt4.place(x=250,y=110)


    B1=Button(F,text="SAVE",relief=GROOVE,bg="light blue",fg="red",command=Create,font=("Arial",10,"bold")).place(x=265,y=140)
    B2=Button(F,text="RESET",relief=GROOVE,bg="light blue",fg="red",command=Clear,font=("Arial",10,"bold")).place(x=350,y=140)
    W1.mainloop()

