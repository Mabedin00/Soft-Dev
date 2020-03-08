"""
Session data:
- "paid" (bool): True if user paid, false if user has not paid. This should be set to False when user finishes a game
- "current_game" (str): This should be the route to the entrance of your game. This should work when you run redirect(url_for(session["current_game"]))
- "bet_amount" (int): Amount the user is betting on the game.

Session is all cleared when user logouts
"""
import os, random
from flask import Flask, session, render_template, redirect, url_for, request, flash
from mongo import *
from pymongo import MongoClient
import random

app = Flask(__name__)
client = MongoClient() 
db = client.MosDB
collection = db.movies

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/gross")
def gross():
    list = get_movies_by_us_gross(request.args['gross'])
    return render_template("home.html", list = list, type = "gross")

@app.route("/year")
def year():
    list = get_movies_by_year(request.args['year'])
    # print(list)
    return render_template("home.html", list = list, type = "year")

@app.route("/rating")
def rating():
    list = get_movies_by_rating(request.args['IMDB'],request.args['Rotten_Tomatoes'])
    # print(list)
    return render_template("home.html", list = list, type = "rating")

@app.route("/genre")
def genre():
    list = get_movies_by_genre(request.args['genre'])
    return render_template("home.html", list = list, type = "genre")

if __name__ == "__main__":
    app.debug = True
    app.run()
