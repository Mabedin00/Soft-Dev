#Team Drumstick huangT abedinM
#Tyler Huang
#SoftDev1 pd2
#K12: Echo Echo Echo
#2019-09-27

from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route("/")
def helloWorld():
    print(app)
    return render_template(
        "landingpage.html"
    )

@app.route("/auth")
def authenticate():
    print(app)
    print("--------------------")
    print(request)
    print("--------------------")
    print("method " + request.method)
    print("--------------------")
    print(request.form)
    print("--------------------")
    print(request.args)
    print("--------------------")
    print(request.args['username'])
    print("--------------------")
    #print(request.headers)
    return render_template(
        "responsepage.html",
        user = request.args['username'],
        method = request.method,
        greeting = "leave"
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
