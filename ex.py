import sqlite3 as sql
import sys
#uno=input("uno")
#name=input("name")
con=sql.connect('ex.db')
cur=con.cursor()
#cur.execute("create table student(uno int(11),name varchar(20),primary key(uno))")
#st="select * from student"
#st="insert into student(uno,name) values(306,'harish')"
#cur.execute(st)
#rows=cur.fetchall()
#con.commit()
cur.execute("drop table student")
con.close()
#print("UUCMS\t|NAME")
#for row in rows:
  #  uno=row[0]
   # name=row[1]
    #print(f"{uno}\t|{name}|")