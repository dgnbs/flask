from flask import Flask

app=Flask(__name__)

@app.route("/")
def homePage():
    return "<h1>Welcome to my homepage</h1>"

@app.route("/aboutus")
def message():
    return "Hello my friends"

@app.route("/nbs")
def boom():
    return "Welcome to Nationwide"

app.run()