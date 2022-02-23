from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def homePage():

    return render_template("inputform.html")

@app.route("/data",methods=["POST"])
def process():

    a=int(request.form["num1"])
    b=int(request.form["num2"])


    return render_template("timestable.html", t=a,r=b)

app.run(debug=True)