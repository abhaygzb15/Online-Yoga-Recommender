#Admin Module (Login)
import mysql.connector
def DisplayRec_Login():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     cur.execute("Select * From login")
     records=cur.fetchall()
     print("*"*80)
     print("Name \t\t|  Username\t| Password | Date of Birth")
     print("*"*80)
     for i in records:
          print(i[0],"\t|",i[1].ljust(8),"\t|",i[2],"  |",i[3])
#DisplayRec_Login()
#print("*"*80)
def Authorization_Login():
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
#Authorization_Login()

def Insertion_Login():
     conn=mysql.connector.connect(host="localhost",user="root",
          password="tiger",database="project")
     cur=conn.cursor()
     print("*"*80)
     Name=input("ENTER YOUR NAME, ex - Abc_ad \t\t:\t")
     U_Name=input("ENTER THE USERNAME, ex - Abc@info.in \t:\t")
     pwd=input("ENTER YOUR PASSWORD (6 digits)\t\t:\t")
     dob=input("ENTER DATE OF BIRTH (YYYY-MM-DD)\t:\t")
     print("*"*80)
     query="INSERT INTO Login VALUES ('{}','{}','{}','{}')".format(Name,U_Name,pwd,dob)
     cur.execute(query)
     cur.execute("commit")
     print("\t\t\t RECORD INSERTED SUCCESSFULLY")
     print("*"*80)

#Insertion_Login()    
     
