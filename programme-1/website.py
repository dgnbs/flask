from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def homePage():
    return  render_template("home.html")

@app.route("/team")
def message():
    return  render_template("team.html")

@app.route("/services")
def boom():
    return render_template("services.html")

app.run()