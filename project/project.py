from flask import Flask, redirect, render_template, request
import mysql.connector

app=Flask(__name__)
db=mysql.connector.connect( host="localhost",
                            user="root",
                            password="root",
                            database="nbs"
                            )

mycursor= db.cursor()

@app.route("/")
def homePage():
    mycursor.execute("Select * from personal2")
    records=mycursor.fetchall();

    return render_template("homepage.html",data=records)

@app.route("/deptEmployees",methods=["post"])
def deptEmployees():
    dept=request.form["dept"]
    if dept=="all":
        mycursor.execute("Select * from personal2")
    else:
        mycursor.execute("Select * from personal2 where department='"+dept+"'")
    records=mycursor.fetchall();
    return render_template("homepage.html",data=records)

@app.route("/departments/<dept>")
def departmentlist(dept):
    mycursor.execute("Select * from personal2 where department='"+dept+"'")
    records=mycursor.fetchall();

    return render_template("homepage.html",data=records)

@app.route("/newrecord")
def newrecord():
    return render_template("inputform.html")

@app.route("/saverecord",methods=["post"])
def saverecord():
    name=request.form["na"]
    dept=request.form["dept"]
    sql1="insert into personal2(name,department) values('{0}','{1}')".format(name,dept)
    mycursor.execute(sql1)
    db.commit()
    return redirect("/")

@app.route("/details/<empno>")
def details(empno):
    mycursor.execute("Select * from personal2 where empno="+empno)
    personalrecord=mycursor.fetchall();
    mycursor.execute("Select * from accounts where empno="+empno)
    salaryrecords=mycursor.fetchall();
    print(salaryrecords)
    return render_template("details.html",personal=personalrecord,accounts=salaryrecords)

@app.route("/salary")
def salary():
    return render_template("salary.html")

@app.route("/newsalary", methods=["post"])
def newsalary():
    salary=request.form["salary"]
    empno=request.form["empno"]
    sql2="insert into accounts (empno,salary,date) values ('{0}','{1}',now())".format(empno,salary)
    mycursor.execute(sql2)
    db.commit()
    return redirect("/salary.html")

app.run(debug=True)