import pymysql as p
 
def connect():
   
    return p.connect(host="localhost",user="root",password="",database="portfolio")
 
 
 
def addrec(t):
    db=connect()
    cr=db.cursor()
    sql="insert into resume values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

#admin
def detailsrec():
    db=connect()
    cr=db.cursor()
    sql="select * from resume"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data


#admin
def updaterec(t):
    db=connect()
    cr=db.cursor()
    sql="update resume set name=%s,email=%s,contact=%s,objective=%s,Board10=%s,school10=%s,marks10=%s,passingyear10=%s,board12=%s,school12=%s,marks12=%s,stream12=%s,passingyear12=%s,graduations=%s,cgpa=%s,graduationcoll=%s,graduationpy=%s,masters=%s,mscgpa=%s,mastercoll=%s,masterpy=%s,project=%s,skills=%s,dob=%s,address=%s,language=%s,link=%s where email=%s"
    cr.execute(sql,t)
    db.commit()
    db.close()
#admin 
def selectrec(email):
    db=connect()
    cr=db.cursor()
    sql="select * from resume where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0]
 
 
#ADmin delete 
def deleterec(email):
    db=connect()
    cr=db.cursor()
    sql="delete from resume where email=%s"
    cr.execute(sql,email)
    db.commit()
    db.close()      
 
#user select 
def selectrec1(email):
    db=connect()
    cr=db.cursor()
    sql="select email,contact from resume where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
 

#user select 
def selectrec2(email):
    db=connect()
    cr=db.cursor()
    sql="select * from resume where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data


#user
def userrex(email):
    db=connect()
    cr=db.cursor()
    sql="select * from resume where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
