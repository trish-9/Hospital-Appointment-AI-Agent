#import pandas as pd 
import sqlite3 as sq
from bardapi import Bard
import pandas as pd 
from twilio.rest import Client
account_sid = "fewewff"#enter ssid 
auth_token  = "pwoweovv"#enter token no 

client = Client(account_sid, auth_token)

s =sq.connect("tr.db")
s.execute("create table pat(id integer primary key , name varchar(30),age integer , doctor varchar(30),date varchar(30),time varchar(30));")
s4 = pd.read_sql('select* from pat;',s)
li = len(s4['id'])
while True:
   print("Welcome to Ai Agent  Book An Appointment")
   print("1. TO BOOK AN APPOINTMENT \
       2. TO RESHDEULE APPOINTMENT \
       3. TO CANCEL THE APPOINTMENT \
       4. EXIT")
   o = int(input("ENTER THE NUMBER TO CONTINUE"))
   if o == 1:
     n = input('ENTER THE DATE[YYYY-DD-MM]')
     n1 = input('ENTER THE DOCTOR TYPE --- Cardiologist , Dermatologist , Neurologist , Genral Physician')
     n2 = input('ENTER THE NAME OF PATIENT')
     n3 = input("ENTER THE TIME SLOT -- Morning[10:00-12:00] , Afternoon[2:00-4:00] , Evening[5:00-7:00]" )
     n4 = input("ENTER THE AGE")
     s2 = pd.read_sql(f"select id from pat where doctor = '{n1}' and date = '{n}' and time = '{n3}' ;",s)
     if s2.empty == True:
        s4 = pd.read_sql('select* from pat;',s)
        if len(s4['id']) == 0:
           s.execute(f'insert into pat(id , name,age,doctor,date , time ) values(1,"{n2}",{n4},"{n1}","{n}","{n3}");')
           s.commit()
           message = client.messages.create(to="+918000735960",from_="+18148882474",body=f"Hi {n2} Your Slot is Booked in {n3} on {n}")
        else:
           s.execute(f'insert into pat(id , name,age,doctor,date , time ) values({li+1},"{n2}",{n4},"{n1}","{n}","{n3}");')
           s.commit()
           message1 = client.messages.create(to="+918000735960",from_="+18148882474",body=f"Hi {n2} Your Slot is Booked in {n3} on {n}")
     else:
       print("SOORY NO SOLTS AVAIABLE ON THIS DATE ")
       n5 = input("PLEASE ENTER DATE ")
       n6 = input("PLEASE ENTER DOCTOR ")
       n7 = input("ENTER THE TIME SLOT  ")
       o1 = pd.read_sql(f"select time from pat where doctor = '{n6}' and date = '{n5}' and time = '{n7}'; ",s )
       l = []
       for a in o1['time']:
           l.append(a)
#print(l[0])
#print(l)
   
       if len(l) == 0:
       #print("avible")
          s.execute(f'insert into pat(id , name,age,doctor,date , time ) values(1,"{n2}",{n4},"{n1}","{n5}","{n3}");')
          s.commit()
          message3 = client.messages.create(to="+918000735960",from_="+18148882474",body=f"Hi {n2} Your Slot is Booked in {n7} on {n5}")
       else: 
         while l[0] == n7 :
        
           n5 = input("PLEASE ENTER DATE ")
           n6 = input("PLEASE ENTER DOCTOR ")
           n7 = input("ENTER THE TIME SLOT  ")
    #o = pd.read_sql(f"select time from pat where doctor = '{d}' and date = '{n}' and time = {t} ; ",s )
       s.execute(f'insert into pat(id , name,age,doctor,date , time ) values({li+1},"{n2}",{n4},"{n1}","{n5}","{n3}");')
       s.commit()
       message4 = client.messages.create(to="+918000735960",from_="+18148882474",body=f"Hi {n2} Your Slot is Booked in {n7} on {n5}")
   if o == 4:
     exit()
   if o == 2:
      n8 = input("PLEASE ENTER DATE ")
      n9 = int(input("PLEASE ENTER AGE  "))
      n10 = input("ENTER THE TIME SLOT  ")
      n11 = input("ENTER THE NAME OF PATIENT ")
      n12 = input("ENTER THE DOCTOR ")
      o2 = pd.read_sql(f"select time from pat where doctor = '{n6}' and date = '{n5}' and time = '{n7}'; ",s )
      l1 = []
      if len(l1) == 0:
       
          s.execute(f"update pat set date = '{n8}' , time = '{n10}' where name = '{n11}' and age = {n9} and doctor = '{n12}' ;")
          s.commit()
          message5 = client.messages.create(to="+918000735960",from_="+18148882474",body=f"Hi {n2} Your Slot is Updated ,It Will be Reshdeual in {n7} on {n5}")
      else:
       for c in o2['time']:
           l1.append(c)
       while l1[0] == n10 :
           n8 = input("PLEASE ENTER DATE ")
           n10 = input("ENTER THE TIME SLOT  ")
           n12 = input("ENTER THE DOCTOR ")
       s.execute(f"update pat set date = '{n8}' , time = '{n10}' where name = '{n11}' and age = {n9} and doctor = '{n12}' ;")
       s.commit()
       message6 = client.messages.create(to="+918000735960",from_="+18148882474",body=f"Hi {n2} Your Slot is Updated ,It Will be Reshdeual in {n7} on {n5}")
   if o == 3:
      n13 = input("ENTER THE NAME ")
      n14 = int(input("ENTER THE AGE "))
      n51 = input("ENTER THE DATE ")
      n71 = input("ENTER THE TIME ")
      s.execute(f"delete from pat where name = '{n13}' and age = {n14}")
      s.commit()
      message7 = client.messages.create(to="+918000735960",from_="+18148882474",body=f"Hi {n13} Your Slot is Canceled that was  on {n51}  in  {n71}")
        
         
   
       
