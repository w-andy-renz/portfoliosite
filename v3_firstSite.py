from flask import Flask, render_template
from bokeh.embed import server_document
import pandas

app = Flask(__name__)

app.config["UPLOAD_DIRECTORY"] = 'uploads'

@app.route('/plot/')
def plot():
    js_script = server_document("https://test-andyrenz.herokuapp.com/")
    print(js_script)
    return render_template("plot.html", js_script=js_script)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/webcam-detector/')
def webcam_detector():
    return render_template("webcam_detector.html")

@app.route('/mobile-app/')
def mobile_app():
    return render_template("mobile-app.html")

@app.route('/dnd-app/')
def dnd():
    return render_template("dnd.html")

@app.route('/geomap/')
def geomap():
    return render_template("geomap.html", map=True)

@app.route('/dictionary/')
def dictionary():
    return render_template("dictionary.html")

@app.route('/desktop-database-app/')
def desktop_database_app():
    return render_template("desktop-database-app.html")

@app.route('/webscraper/')
def webscraper():
    df = pandas.read_csv("uploads/Webscraped.csv")
    df = df.drop(columns=['Unnamed: 0'])
    df_html = df.to_html(index=False)
    return render_template("webscraper.html", data=df_html)

if __name__ == "__main__":
    app.run(debug = True)