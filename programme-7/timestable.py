from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def page1():
    return  render_template("page1.html")

@app.route("/page2/<t>")
def page2(t):
    return  render_template("page2",TimesTable="t")

app.run(debug=True)