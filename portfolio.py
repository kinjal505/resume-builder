import email
from re import X
from flask import *
from sql import *

app=Flask(__name__)

@app.route("/")

#home page
@app.route("/home")
def home():
  return render_template("home.html")

#details page
'''
@app.route("/details")
def details():
  x=detailsrec() 
  return render_template("details.html",listdata=x)
'''
#user login page
@app.route("/login")
def login():
    return render_template("login.html")

#user login validate
@app.route("/log",methods=["post"])
def log():
  email=request.form["email"]
  contact=request.form["contact"]
  t1=selectrec1(email)
  user=userrex(email)
  if (email,int(contact)) in t1:
    return render_template("userdetail.html",listdata=user)
  else:
    return redirect("/") 

#user detail
@app.route("/udetail")
def user():
    return render_template("userdetail.html")


#admin login page
@app.route("/admin")
def adm():
    return render_template("admin.html")

#admin login validate
@app.route("/adminvalid")
def admin():
  username=request.args.get("username")
  password=request.args.get("password")
  if (username=='kinjal@gmail.com' and password=='123'):
    return redirect("/cv")
  else:
    return redirect("/")

#add  page
@app.route("/register")
def reg():
    return render_template("register.html")

# inserting record
@app.route("/insert",methods=["post"])
def insert():
  name=request.form["name"]
  email=request.form["email"]
  contact=request.form["contact"]
  objective=request.form["objective"]
  Board10=request.form["Board10"]
  school10=request.form["school10"]
  marks10=request.form["marks10"]
  passingyear10=request.form["passingyear10"]
  board12=request.form["Board12"]
  school12=request.form["school12"]
  marks12=request.form["marks12"]
  stream12 =request.form["stream12"]
  passingyear12=request.form["passingyear12"]
  graduations=request.form["graduations"]
  cgpa=request.form["cgpa"]
  graduationcoll=request.form["graduationcoll"]
  graduationpy=request.form["graduationpassingyear"]
  masters=request.form["masters"]
  mscgpa=request.form["mscgpa"]
  mastercoll=request.form["mastercoll"]
  masterpy=request.form["masterpassingyear"]
  project=request.form["project"]
  skills=request.form["skills"]
  dob=request.form["dob"]
  address=request.form["address"]
  language=request.form["language"]
  link=request.form["link"]
  t=(name,email,contact,objective,Board10,school10,marks10,passingyear10,board12,school12,marks12,stream12,passingyear12,graduations,cgpa,graduationcoll,graduationpy,masters,mscgpa,mastercoll,masterpy,project,skills,dob,address,language,link)
  addrec(t)
  return redirect("login")

#admin edit
@app.route("/edit")
def edit():
  emailid=request.args.get("email")
  print(emailid)
  y=selectrec(emailid)
  return render_template("edit.html",listdata=y)

# admin updating
@app.route("/updating",methods=["post"])
def update():
  name=request.form["name"]
  email=request.form["email"]
  contact=request.form["contact"]
  objective=request.form["objective"]
  Board10=request.form["Board10"]
  school10=request.form["school10"]
  marks10=request.form["marks10"]
  passingyear10=request.form["passingyear10"]
  board12=request.form["Board12"]
  school12=request.form["school12"]
  marks12=request.form["marks12"]
  stream12 =request.form["stream12"]
  passingyear12=request.form["passingyear12"]
  graduations=request.form["graduations"]
  cgpa=request.form["cgpa"]
  graduationcoll=request.form["graduationcoll"]
  graduationpy=request.form["graduationpassingyear"]
  masters=request.form["masters"]
  mscgpa=request.form["mscgpa"]
  mastercoll=request.form["mastercoll"]
  masterpy=request.form["masterpassingyear"]
  project=request.form["project"]
  skills=request.form["skills"]
  dob=request.form["dob"]
  address=request.form["address"]
  language=request.form["language"]
  link=request.form["link"]
  t=(name,email,contact,objective,Board10,school10,marks10,passingyear10,board12,school12,marks12,stream12,passingyear12,graduations,cgpa,graduationcoll,graduationpy,masters,mscgpa,mastercoll,masterpy,project,skills,dob,address,language,link,email)
  updaterec(t)
  return redirect("/cv")

#delete record
@app.route("/delete")
def delete():
  email1=request.args.get("email")
  deleterec(email1)
  return redirect("/cv")

#admin  page
@app.route("/cv")
def usercv():
  U=detailsrec()
  print(U)
  return render_template("cv.html",listdata=U)


if __name__=="__main__":
    app.run(debug=True)
