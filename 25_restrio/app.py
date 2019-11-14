from flask import Flask, render_template
import urllib, json
import random

app = Flask(__name__) #create new instance of flask
@app.route("/")
def root():
    u = urllib.request.urlopen("https://restcountries.eu/rest/v2/name/usa")
    #
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", name = response["name"])
#
# @app.route("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
