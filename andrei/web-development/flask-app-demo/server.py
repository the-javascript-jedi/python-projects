# Run code > flask --app server run --debug
from flask import Flask,render_template
# __name__ specifies the name of app - print(__name__) = main
app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World! I want to go to America</p>"
    return render_template('index.html')

@app.route("/<username>")
def username(username=None):
    return render_template('index.html', name=username)

@app.route("/about.html")
def about():
    return render_template('about.html')
