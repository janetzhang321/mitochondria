from flask import Flask, render_template, request
import csv,json,os 
from utils import energy

app = Flask(__name__)
data = energy.get_reports()
schema = energy._test_interfaces()
#print(schema)

@app.route("/", methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/ports", methods=['POST','GET'])
def ports():
    year = request.args.get('year')
    category = str(request.args.get('category'))
    return render_template('ports.html',data=data,year=year,category=category)

if __name__ == '__main__': 
    app.debug = True
    app.run() 
