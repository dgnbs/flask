from flask import Flask

app=Flask(__name__)

@app.route("/")
def homePage():
    return  """
            <html>

            <center><h1>Welcome to my homepage</h1></center>
            We are the world's largest Build Society
            <br>
            <br>
            <a href="http://localhost:5000/team">Who we are</a><br>
            <a href="http://localhost:5000/services">Our services</a><br>

            </html>
            """

@app.route("/team")
def message():
    return  """
            <br>
            <center><h1>Hello my friends</h1></center>
            <br>
            <a href="http://localhost:5000">Home</a>
            """

@app.route("/services")
def boom():
        return  """
            <html>

            <center><h1>We provide the following services</h1></center>
            <br>
            <a href="http://localhost:5000">Home</a>
            <br>
            <ul>
                <li>Open Accounts</li>
                <li>Deposit money</li>
                <li>Withddraw money</li>
            </ul>

            </html>
            """

app.run()