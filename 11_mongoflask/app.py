"""
Session data:
- "paid" (bool): True if user paid, false if user has not paid. This should be set to False when user finishes a game
- "current_game" (str): This should be the route to the entrance of your game. This should work when you run redirect(url_for(session["current_game"]))
- "bet_amount" (int): Amount the user is betting on the game.

Session is all cleared when user logouts
"""
import os, random
from flask import Flask, session, render_template, redirect, url_for, request, flash
import mongo
import random

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.globals.update(get_balance=lambda: database_query.get_balance(session["username"]))
    app.run()
