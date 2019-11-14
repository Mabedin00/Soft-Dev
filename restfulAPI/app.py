from flask import Flask, render_template
import urllib, json

app = Flask(__name__) #create new instance of flask
@app.route("/")
def root():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=VdYsyzgDaCPGB3NbGK23gDxBonpCxadx0lroq37G")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic = data["url"], desc = data["explanation"])

if __name__ == "__main__":
    app.debug = True
    app.run()
