from flask import Flask
app = Flask(__name__) #create new instance of flask
@app.route("/")
def hello_world():
    print(__name__)
    return "No"
@app.route("/different")
def different():
    return "different route"

@app.route("/something/")
def something():
    return "we go againasdawdaw"

if __name__ == "__main__":
    app.debug = True
    app.run()
