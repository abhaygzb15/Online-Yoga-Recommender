import pyfiglet
import mysql.connector
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
W=''

def STYLES(x):
    res=pyfiglet.figlet_format(x,font="digital")# Use standard,digital,bubble,etc fonts.

    print("*"*80)
    print(res)
    print("*"*80)

def Registera():
    W.destroy()
    from USER import User_Login as J1
    J1.Register()
    Main()
    
def admin():
    STYLES("    WELCOME TO YOGA RISING APPLICATION")
    print("\t\t\t  ADMIN LOGIN ")
    while True:
        from ADMIN import admin_login as M1
        if (M1.Authorization_Login())==True: #if admin_module_login.Authorization_Login()==True:
            while True:
                print("*"*80)
                print("\t\t\t 1.TABLE LOGIN")
                print("\t\t\t 2.TABLE-DISEASES")
                print("\t\t\t 3.TABLE-CENTRES")
                print("\t\t\t 4.EXIT")
                print("*"*80)
                ch=int(input("ENTER THE CHOICE \t:\t"))
                print("*"*80)
                if ch==1:
                    STYLES("            LOGIN TABLE")
                    while ch<3:
                        print("*"*80)
                        print("\t\t\t 1. DISPLAYING OF RECORDS")
                        print("\t\t\t 2. INSERTION OF RECORDS")
                        print("\t\t\t 3. EXIT")
                        print("*"*80)
                        ch=int(input("ENTER THE CHOICE\t:\t"))
                        print("*"*80)
                        if ch==1:
                            M1.DisplayRec_Login()
                        if ch==2:
                            M1.Insertion_Login()   
                    else:
                        continue
                if ch==2:
                    from ADMIN import admin_diseases as M2
                    STYLES("             DISEASES TABLE")
                    while ch<4:
                        print("*"*80)
                        print("\t\t\t 1.INSERTION OF RECORDS")
                        print("\t\t\t 2.UPDATION OF RECORDS")
                        print("\t\t\t 3.DELETION OF RECORDS")
                        print("\t\t\t 4.EXIT")
                        print("*"*80)
                        ch=int(input("ENTER THE CHOICE\t:\t"))
                        print("*"*80)
                        if ch==1:
                            M2.Insertion_Diseases()
                        if ch==2:
                            M2.Updation_Diseases()
                        if ch==3:
                            M2.Deletionmain_Diseases()
                    else:
                        continue
                if ch==3:
                    from ADMIN import admin_centres as M3
                    STYLES("                  CENTRES TABLE")
                    while ch<4:
                        print("*"*80)
                        print("\t\t\t 1.INSERTION OF RECORDS")
                        print("\t\t\t 2.UPDATION OF RECORDS")
                        print("\t\t\t 3.DELETION OF RECORDS")
                        print("\t\t\t 4.EXIT")
                        print("*"*80)
                        ch=int(input("ENTER THE CHOICE\t:\t"))
                        print("*"*80)
                        if ch==1:
                            M3.Insertion_Centres()
                        if ch==2:
                            M3.Updation_Centres()
                        if ch==3:
                            M3.Deletionmain_Centres()
                    else:
                        continue
                if ch==4:
                    break
            STYLES("    STAY    HEALTHY   AND   KEEP    VISITING               YOGA    RISING    APPLICATION")
            break

def Author_Login():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     u=input("ENTER THE USERNAME \t:\t")
     p=input("ENTER THE PASSWORD \t:\t")
     print("*"*80)
     query="select username,password from login where username='{}' and password='{}'".format(u,p)
     cur.execute(query)
     records=cur.fetchall()
     if records==[]:
          print("\t\t Login failed! Try Again")
          print("*"*80)
     else:
          print("\t\t Successfully Login!! Go ahead")
          print("*"*80)
          return True

def user():
    STYLES("    WELCOME TO YOGA RISING APPLICATION")
    W.destroy()
    while True:
        if Author_Login()==True:
            from USER import User_Choices as M5
            M5.User_Searching()
            break

def Main():
    global W
    W=Tk()
    W.geometry("840x540")
    W.configure(bg="#FFA500")
    W.title("INITIAL SCREEN")
    image=Image.open("Yon.jpg")
    R=image.resize((460,250))
    R2=ImageTk.PhotoImage(R)
    Lb=Label(W,image=R2)
    Lb.place(x=190,y=74)

    L1=Label(W,text="  Y O G A     R I S I N G      A P P L I C A T I O N ",bg="light green",font=("TIMES NEW ROMAN",24,"bold"))
    L1.pack(fill=BOTH,padx=0,pady=0)
    image1=Image.open("YO.jpg")
    Ra=image1.resize((160,250))
    Rb=ImageTk.PhotoImage(Ra)
    Lb1=Label(W,image=Rb)
    Lb1.place(x=10,y=80)

    i=Image.open("GA.png")
    Ri=i.resize((160,250))
    Rj=ImageTk.PhotoImage(Ri)
    Lbi=Label(W,image=Rj)
    Lbi.place(x=670,y=80)
    F=Frame(height=200,bg="#FF7F50",width=700,border=1)
    F.place(x=68,y=345)

    Ls=Label(W,text="CHOOSE YOUR CHOICE OUT OF THE THREE ",bg="#A52A2A",font=("TIMES NEW ROMAN",24,"bold"))
    Ls.place(x=78,y=355)
    B1=Button(F,text="ADMIN LOGIN ",relief=GROOVE,bg="Red",fg="black",command=admin,font=("Arial",15,"bold")).place(x=30,y=100)
    B2=Button(F,text="USER REGISTER",relief=GROOVE,bg="Red",fg="black",command=Registera,font=("Arial",15,"bold")).place(x=230,y=100)
    B3=Button(F,text="USER LOGIN",relief=GROOVE,bg="Red",fg="black",command=user,font=("Arial",15,"bold")).place(x=460,y=100)
    W.mainloop()
Main()

