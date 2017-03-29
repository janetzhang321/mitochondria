from flask import Flask, render_template
import csv
from utils import energy

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/ports")
def ports():
    data = energy._test_interfaces()
    print(data)
    return render_template('ports.html')

if __name__ == '__main__': 
    app.debug = True
    app.run() 
