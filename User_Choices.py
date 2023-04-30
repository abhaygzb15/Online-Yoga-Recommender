import mysql.connector
from PIL import Image
import webbrowser
import urllib
import urllib.parse
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import pyfiglet

def Meditation():
     url2='https://www.nccih.nih.gov/health/meditation-in-depth'
     webbrowser.open(url2)
#Meditation()

def User_Diseases():
     conn=mysql.connector.connect(host="localhost",user="root",password="tiger",database="project")
     cur=conn.cursor()
     n=0
     while True:
          q="select Sno,diseases from diseases"
          cur.execute(q)
          for i in cur:
               print("\t\t\t",i[0],".",i[1].upper())
          print("\t\t\t 6 . EXIT")
          print("*"*100)
          ch=int(input("ENTER THE CHOICE \t\t:\t"))
          print("*"*100)
          if ch==1:
               query="SELECT symptoms from diseases where diseases= 'Asthma'"
               cur.execute(query)
               rec=cur.fetchone()
               m1=rec[0]
               print("1.SYMPTOMS OF A DISEASE \t:\t",m1)
          
               query="SELECT yoga_asanas  from diseases where diseases= 'Asthma'"
               cur.execute(query)
               rec=cur.fetchone()
               m2=rec[0]
               print("2.YOGA ASANA \t\t\t:\t",m2)

               query="SELECT diet_offered from diseases where diseases= 'Asthma'"
               cur.execute(query)
               rec=cur.fetchone()
               m3=rec[0]
               print("3.DIET REQUIRED FOR A DISEASE \t:\t",m3)

               F=Image.open("Uttanasana.jpg" )
               F.show()
               print("*"*100)
               

          if ch==2:
               query="SELECT symptoms from diseases where diseases= 'Arthritis'"
               cur.execute(query)
               rec=cur.fetchone()
               m1=rec[0]
               print("1.SYMPTOMS OF A DISEASE \t:\t",m1)
          
               query="SELECT yoga_asanas  from diseases where diseases= 'Arthritis'"
               cur.execute(query)
               rec=cur.fetchone()
               m2=rec[0]
               print("2.YOGA ASANA \t\t\t:\t",m2)

               query="SELECT diet_offered from diseases where diseases= 'Arthritis'"
               cur.execute(query)
               rec=cur.fetchone()
               m3=rec[0]
               print("3.DIET REQUIRED FOR A DISEASE \t:\t",m3)

               F=Image.open("Vrikshasana.png" )
               F.show()
               print("*"*100)
              
               
               
          if ch==3:
               query="SELECT symptoms from diseases where diseases= 'Thyroid'"
               cur.execute(query)
               rec=cur.fetchone()
               m1=rec[0]
               print("1.SYMPTOMS OF A DISEASE \t:\t",m1)
          
               query="SELECT yoga_asanas  from diseases where diseases= 'Thyroid'"
               cur.execute(query)
               rec=cur.fetchone()
               m2=rec[0]
               print("2.YOGA ASANA \t\t\t:\t",m2)

               query="SELECT diet_offered from diseases where diseases= 'Thyroid'"
               cur.execute(query)
               rec=cur.fetchone()
               m3=rec[0]
               print("3.DIET REQUIRED FOR A DISEASE\t:\t",m3)

               F=Image.open("bandhasana.png" )
               F.show()
               print("*"*100)
               
               
          if ch==4:
               query="SELECT symptoms from diseases where diseases= 'Migraine'"
               cur.execute(query)
               rec=cur.fetchone()
               m1=rec[0]
               print("1.SYMPTOMS OF A DISEASE \t:\t",m1)
          
               query="SELECT yoga_asanas  from diseases where diseases= 'Migraine'"
               cur.execute(query)
               rec=cur.fetchone()
               m2=rec[0]
               print("2.YOGA ASANA \t\t\t:\t",m2)

               query="SELECT diet_offered from diseases where diseases= 'Migraine'"
               cur.execute(query)
               rec=cur.fetchone()
               m3=rec[0]
               print("3.DIET REQUIRED FOR A DISEASE \t:\t",m3)

               F=Image.open("shishuasana.png" )
               F.show()
               print("*"*100)
              

          if ch==5:
               query="SELECT symptoms from diseases where diseases= 'Diabetes'"
               cur.execute(query)
               rec=cur.fetchone()
               m1=rec[0]
               print("1.SYMPTOMS OF A DISEASE \t:\t",m1)
          
               query="SELECT yoga_asanas  from diseases where diseases= 'Diabetes'"
               cur.execute(query)
               rec=cur.fetchone()
               m2=rec[0]
               print("2.YOGA ASANA \t\t\t:\t",m2)

               query="SELECT diet_offered from diseases where diseases= 'Diabetes'"
               cur.execute(query)
               rec=cur.fetchone()
               m3=rec[0]
               print("3.DIET REQUIRED FOR A DISEASE \t:\t",m3)

               F=Image.open("Tadasana.png" )
               F.show()
               print("*"*100)
               
                   
          if ch==6:
               break

User_Diseases()

def User_YogaCentres():
     conn=mysql.connector.connect(host="localhost",user="root",password="tiger",database="project")
     cur=conn.cursor()
     n=0
     while True:
          quer="SELECT sno,centre_name from centres"
          cur.execute(quer)
          for i in cur:
               print("\t\t\t",i[0],".",i[1].upper())
          print("\t\t\t 5 . EXIT")
          print("*"*100)
          ch=int(input("ENTER THE CHOICE \t\t:\t"))
          print("*"*100)
          if ch==1:
               query="SELECT * from centres where centre_name='Satwa Yoga Studio'"
               cur.execute(query)
               rows=cur.fetchall()
               for i in rows:
                    print("ADDRESS OF THE CENTRE \t:\t",i[2])
                    print("CONTACT OF THE CENTRE \t:\t",i[3])
                    print("EMAIL-ID OF THE CENTRE \t:\t",i[4])
                    print("TIMINGS OF THE CENTRE \t:\t",i[5])
                    print("MEMBERSHIP FEES OFFERED :\t",i[6])
                    print("*"*100)
              
          if ch==2:
               query="SELECT * from centres where centre_name='Yoga Mantra'"
               cur.execute(query)
               rows=cur.fetchall()
               for i in rows:
                    print("ADDRESS OF THE CENTRE \t:\t",i[2])
                    print("CONTACT OF THE CENTRE \t:\t",i[3])
                    print("EMAIL-ID OF THE CENTRE \t:\t",i[4])
                    print("TIMINGS OF THE CENTRE \t:\t",i[5])
                    print("MEMBERSHIP FEES OFFERED :\t",i[6])
                    print("*"*100)
            

          if ch==3:
               query="SELECT * from centres where centre_name='Sivananda Yoga Vedanta Centre'"
               cur.execute(query)
               rows=cur.fetchall()
               for i in rows:
                    print("ADDRESS OF THE CENTRE \t:\t",i[2])
                    print("CONTACT OF THE CENTRE \t:\t",i[3])
                    print("EMAIL-ID OF THE CENTRE \t:\t",i[4])
                    print("TIMINGS OF THE CENTRE \t:\t",i[5])
                    print("MEMBERSHIP FEES OFFERED :\t",i[6])
                    print("*"*100)
            

          if ch==4:
               query="SELECT * from centres where centre_name='The Yoga House'"
               cur.execute(query)
               rows=cur.fetchall()
               for i in rows:
                    print("ADDRESS OF THE CENTRE \t:\t",i[2])
                    print("CONTACT OF THE CENTRE \t:\t",i[3])
                    print("EMAIL-ID OF THE CENTRE \t:\t",i[4])
                    print("TIMINGS OF THE CENTRE \t:\t",i[5])
                    print("MEMBERSHIP FEES OFFERED :\t",i[6])
                    print("*"*100)
               
          if ch==5:
               break

#User_YogaCentres()

def Screen():
     def Link1():
          url1='http://www.mea.gov.in/in-focus-article.htm?25096/Yoga+Its+Origin+History+and+Development'
          webbrowser.open(url1)

     def Link2():
          Link="https://www.youtube.com/watch?v=_8kV4FHSdNA"
          webbrowser.open(Link)
          W.destroy()

     W=Tk()
     W.geometry("840x540")
     W.configure(bg="yellow")
     W.title("WORKING SCREEN")
     
     image=Image.open("New1.png")
     R=image.resize((760,250))
     R2=ImageTk.PhotoImage(R)
     Lb=Label(W,image=R2)
     Lb.place(x=32,y=66)


     L1=Label(W,text="  Y O G A     R I S I N G      A P P L I C A T I O N ",bg="light green",font=("TIMES NEW ROMAN",24,"bold"))
     L1.pack(fill=BOTH,padx=0,pady=0)

     F=Frame(height=200,bg="#FF7F50",width=350,border=1)
     F.place(x=32,y=335)

     Fl=Frame(height=200,bg="#FF7F50",width=350,border=1)
     Fl.place(x=445,y=335)
     
     L2=Label(W,text="  HISTORY OF YOGA AND ITS INFLUENCE ",bg="light blue",font=("Comic Sans MS",11,"bold"))
     L2.place(x=34,y=338)

     L4=Label(W,text="  THROUGH READING ON CHROME ",bg="#FFEFD5",font=("Comic Sans MS",11,"bold"))
     L4.place(x=60,y=400)

     L3=Label(W,text="  HISTORY OF YOGA AND ITS INFLUENCE ",bg="cyan",font=("Comic Sans MS",11,"bold"))
     L3.place(x=447,y=338)

     L5=Label(W,text="  THROUGH WATCHING ON YOUTUBE ",bg="#FFEFD5",font=("Comic Sans MS",11,"bold"))
     L5.place(x=460,y=395)

     B1=Button(F,text="GO",relief=GROOVE,bg="light blue",fg="red",command=Link1,font=("Arial",30,"bold")).place(x=130,y=110)
     B2=Button(Fl,text="GO",relief=GROOVE,bg="light blue",fg="red",command=Link2,font=("Arial",30,"bold")).place(x=120,y=110)
     W.mainloop()
#Screen()

def STYLES(x):
    res=pyfiglet.figlet_format(x,font="digital")# Use standard,digital,bubble,etc fonts.

    print("*"*80)
    print(res)
    print("*"*80)
     
def User_Searching():
     print("*"*100)
     while True:
          print("\t\t\t 1.INFORMATION ABOUT YOGA AND IT'S HISTORY")
          print("\t\t\t 2.DISEASES AND THEIR CURING")
          print("\t\t\t 3.MEDITATION - A BRANCH OF YOGA")
          print("\t\t\t 4.BEST YOGA CENTRES IN INDIA")
          print("\t\t\t 5.EXIT")
          print("*"*100)
          ch=int(input("ENTER THE CHOICE\t\t:\t"))
          print("*"*100)
          if ch==1:
               Screen()
          if ch==2:
               User_Diseases()
          if ch==3:
               Meditation()
          if ch==4:
               User_YogaCentres()
          if ch==5:
               STYLES("    STAY    HEALTHY   AND   KEEP    VISITING               YOGA    RISING    APPLICATION")
               break
#User_Searching()
