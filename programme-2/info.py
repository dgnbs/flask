from flask import Flask, render_template
app=Flask(__name__)

@app.route("/info1")
def homePage1():
    return  render_template("information.html", na="Shafeeq", addr="Manchester", color="red")

@app.route("/info2")
def homePage2():
    return  render_template("information.html", na="James", addr="London", color="blue")

@app.route("/info3")
def homePage3():
    return  render_template("information.html", na="Angus", addr="Scotland", color="green")

app.run()