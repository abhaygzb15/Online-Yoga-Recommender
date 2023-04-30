#Admin Module (Diseases Table)
import mysql.connector
def DisplayRec_Diseases():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*121)
     cur.execute("Select * From diseases")
     records=cur.fetchall()
     for i in records:
          print(i[0],i[1],i[2],i[3],i[4],sep="  |  ")
          print("*"*121)
#DisplayRec_Diseases()

def GetAdmno_Diseases():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     query="SELECT SNO FROM diseases order by SNO desc limit 1"
     cur.execute(query)
     a=cur.fetchone()
     return a[0]
     

def Insertion_Diseases():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     SNo=GetAdmno_Diseases()+1
     Dis=input("ENTER THE DISEASE \t\t:\t")
     symp=input("ENTER THE SYMPTOMS \t\t:\t")
     yoga=input("ENTER THE YOGA/ASANA \t\t:\t")
     Diet=input("ENTER THE DIET OFFERED \t\t:\t")
     print("*"*80)
     query="INSERT INTO diseases VALUES({},'{}','{}','{}','{}')".format(SNo,Dis,symp,yoga,Diet)
     cur.execute(query)
     cur.execute("commit")
     print("\t\t\t RECORD INSERTED SUCCESSFULLY")
     print("*"*80)
#Insertion_Diseases()

def Updation_Diseases():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     Dis=input("ENTER THE DISEASE\t\t:\t")
     m1="SELECT * from Diseases where diseases='{}'".format(Dis)
     cur.execute(m1)
     cur.fetchall()
     if cur.rowcount==0:
          print("*"*80)
          print("\t\t    NO RECORD FOUND OF SUCH DISEASE NAME")
          print("*"*80)
     else:
          print("*"*80)
          while True:
               print("\t\t\t  1. UPDATE SYMPTOMS ")
               print("\t\t\t  2. UPDATE YOGA ASANA")
               print("\t\t\t  3. UPDATE DIET OFFERED")
               print("\t\t\t  4. EXIT")
               print("*"*80)
               choice =int(input("ENTER THE CHOICE\t\t:\t"))
               print("*"*80)
               if choice == 1:
                    new_sym= input("ENTER THE SYMPTOMS \t\t:\t")
                    print("*"*80)
                    query= "UPDATE Diseases SET Symptoms ='{}' WHERE Diseases='{}'".format(new_sym,Dis)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice == 2:
                    new_asan= input("ENTER THE YOGA/ASANS \t\t:\t")
                    print("*"*80)
                    query= "UPDATE Diseases SET Yoga_Asanas ='{}' WHERE Diseases='{}'".format(new_asan,Dis)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice == 3:
                    new_diet= input("ENTER THE DIET OFFERED \t\t:\t")
                    print("*"*80)
                    query= "UPDATE Diseases SET diet_offered ='{}' WHERE Diseases='{}'".format(new_diet,Dis)
                    cur.execute(query)
                    cur.execute("commit")
                    print(" \t\t\t RECORD UPDATED SUCCESSFULLY")
                    print("*"*80)
               if choice==4:
                    break
          print("*"*80)

#Updation_Diseases()     

def Deletionmain_Diseases():
     def Deletion(x):
          query="SELECT * FROM Diseases WHERE Diseases = '{}'".format(x)
          cur.execute(query)
          cur.fetchall()
          return cur.rowcount
     conn=mysql.connector.connect(host="localhost",user="root",
               password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     x =input("ENTER THE DISEASE NAME \t:\t")
     print("*"*80)
     count= Deletion(x)
     if count!= 0:
          query= "DELETE FROM Diseases WHERE Diseases='{}'".format(x)
          cur.execute(query)
          print("\t\t\tRECORD DELETED SUCCESSFULLY")
          print("*"*80)
          cur.execute("commit")
     else:
          print(" \t\t NO RECORD FOUND OF SUCH DISEASE NAME")
          print("*"*80)
#Deletionmain_Diseases()

    


