from flask import Flask,render_template
# name of object - can be anything
# __name__ -
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("tutorial.html")

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    temperature=23
    return {
        "station":station,
        "date":date,
        "temperature":temperature
    }
if __name__ == "__main__":
    app.run(debug=True,port=5001)