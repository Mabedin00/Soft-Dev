from flask import Flask, render_template
from urllib.request import Request, urlopen
import urllib, json, requests
import random

app = Flask(__name__) #create new instance of flask
@app.route("/")
def root():
    u = urllib.request.urlopen("https://restcountries.eu/rest/v2/name/usa")
    response = u.read()
    data = json.loads(response)[0]
    return render_template("index.html", text = data["name"], pic = data["flag"])

@app.route("/pokemon")
def pokeAPI():
    req = Request('https://pokeapi.co/api/v2/pokemon/{id}/'.format(id = random.randint(1,804)), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    data = json.loads(response)

    return render_template("index.html", text = data["name"], pic = data["sprites"]["front_default"])

@app.route("/card")
def pickACard():
    req = Request("https://deckofcardsapi.com/api/deck/new/draw/?count=1", headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    data = json.loads(response)
    name = "{value} of {suit}".format(value = data["cards"][0]["value"], suit = data["cards"][0]["suit"])
    return render_template("index.html", text = name, pic = data["cards"][0]["image"])
if __name__ == "__main__":
    app.debug = True
    app.run()
