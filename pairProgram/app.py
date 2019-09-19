from flask import Flask
app = Flask(__name__) #create new instance of flask
@app.route("/")
def hello_world():
    return "No"

if __name__ == "__main__":
    app.debug = True
    app.run()
