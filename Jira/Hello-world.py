from flask import Flask
# Creating a flask app instance
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world, My name is Yogesh"
app.run("0.0.0.0")

