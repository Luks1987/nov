from flask import Flask, render_template
import datetime
app = Flask(__name__)



@app.route("/")
def index():
    trenutni_cas = datetime.datetime.now()
    return f"<h1>Moja prva spletna stran</h1><p>Blank.Gucci little piggy</p>{trenutni_cas}"


app.route("/about")
def on_about():
    #preberemo datoteko:
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
