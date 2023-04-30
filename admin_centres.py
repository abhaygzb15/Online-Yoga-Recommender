#Admin Module (Centres Table)
import mysql.connector
def DisplayRec_Centres():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*121)
     cur.execute("Select * From centres")
     records=cur.fetchall()
     for i in records:
          print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],sep="  |  ")
          print("*"*121)
#DisplayRec_Centres()

def GetAdmno_Centres():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     query="SELECT SNO FROM centres order by SNO desc limit 1"
     cur.execute(query)
     a=cur.fetchone()
     return a[0]

def Insertion_Centres():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     SNo=GetAdmno_Centres()+1
     Cname=input("ENTER THE CENTRE NAME \t\t:\t")
     addres=input("ENTER THE ADDRESS \t\t:\t")
     cont=input("ENTER THE CONTACT NUMBER \t:\t")
     Email=input("ENTER THE EMAIL ID\t\t:\t")
     Tim=input("ENTER THE TIMINGS\t\t:\t")
     Fees=input("ENTER THE MEMBERSHIP FEES\t:\t")
     print("*"*80)
     query="INSERT INTO Centres VALUES({},'{}','{}','{}','{}','{}','{}')".format(SNo,Cname,addres,cont,Email,Tim,Fees)
     cur.execute(query)
     cur.execute("commit")
     print("\t\t\t RECORD INSERTED SUCCESSFULLY")
     print("*"*80)
#Insertion_Centres()

def Updation_Centres():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     Cnt=input("ENTER THE CENTRE NAME\t:\t")
     print("*"*80)
     m1="SELECT * from Centres where centre_name='{}'".format(Cnt)
     cur.execute(m1)
     cur.fetchall()
     if cur.rowcount==0:
          print("*"*80)
          print("\t\t    NO RECORD FOUND OF SUCH CENTRE NAME")
          print("*"*80)
     else:
          print("*"*80)
          while True:
               print("\t\t\t  1. UPDATE ADDRESS ")
               print("\t\t\t  2. UPDATE TIMINGS")
               print("\t\t\t  3. UPDATE MEMBERSHIP FEES")
               print("\t\t\t  4. UPDATE CONTACT NUMBER")
               print("\t\t\t  5. UPDATE EMAIL ADDRESS")
               print("\t\t\t  6. EXIT")
               print("*"*80)
               choice =int(input("ENTER THE CHOICE\t\t:\t"))
               print("*"*80)
               if choice == 1:
                    new_adr= input("ENTER THE ADDRESS \t\t:\t")
                    print("*"*80)
                    query= "UPDATE Centres SET address ='{}' WHERE centre_name='{}'".format(new_adr,Cnt)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice == 2:
                    new_tim= input("ENTER THE TIMINGS \t\t:\t")
                    print("*"*80)
                    query= "UPDATE Centres SET Timings ='{}' WHERE centre_name='{}'".format(new_tim,Cnt)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice == 3:
                    new_fee= input("ENTER THE MEMBERSHIP FEES \t:\t")
                    print("*"*80)
                    query= "UPDATE Centres SET Membership_fees ='{}' WHERE centre_name='{}'".format(new_fee,Cnt)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice == 4:
                    new_cont= input("ENTER THE CONTACT NUMBER  \t:\t")
                    print("*"*80)
                    query= "UPDATE Centres SET contact ='{}' WHERE centre_name='{}'".format(new_cont,Cnt)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice == 5:
                    new_mail= input("ENTER THE EMAIL ADDRESS \t:\t")
                    print("*"*80)
                    query= "UPDATE Centres SET email_id ='{}' WHERE centre_name='{}'".format(new_mail,Cnt)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice==6:
                    break
          print("*"*80)

#Updation_Centres()     

def Deletionmain_Centres():
     def Deletion(x):
          query="SELECT * FROM Centres WHERE Contact = '{}'".format(x)
          cur.execute(query)
          cur.fetchall()
          return cur.rowcount
     conn=mysql.connector.connect(host="localhost",user="root",
               password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     x =input("ENTER THE CONTACT NUMBER\t:\t")
     print("*"*80)
     count= Deletion(x)
     if count!= 0:
          query= "DELETE FROM Centres WHERE Contact='{}'".format(x)
          cur.execute(query)
          print("\t\t\tRECORD DELETED SUCCESSFULLY")
          print("*"*80)
          cur.execute("commit")
     else:
          print(" \t\t NO RECORD FOUND OF SUCH CONTACT NUMBER")
          print("*"*80)
#Deletionmain_Centres()

    


