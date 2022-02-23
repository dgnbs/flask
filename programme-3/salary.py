from flask import Flask, render_template
app=Flask(__name__)

@app.route("/info1")
def homePage1():
    name1="Shafeeq"
    salary1=1000
    return  render_template("salaryslip.html",name=name1,salary=salary1)

app.run()