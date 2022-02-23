from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def homePage1():
    return  render_template("homepage.html")

@app.route("/timetable/<num>")
def timesTable(num):
    return  render_template("timestable.html", t=int(num))

app.run()