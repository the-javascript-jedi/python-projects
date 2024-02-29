from flask import Flask
# __name__ specifies the name of app - print(__name__) = main
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! I want to go to America</p>"