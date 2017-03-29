from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/ports")
def ports():
    return render_template('ports.html')

if __name__ == '__main__': 
    app.debug = True
    app.run() 
