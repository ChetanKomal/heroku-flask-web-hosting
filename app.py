from flask_restful import Resource,Api,reqparse
from flask import Flask,jsonify,request,redirect, url_for,render_template\


app = Flask(__name__)

@app.route("/")
def home():
    return "CHETAN VERMA"


if __name__ == "__main__":
    app.run(debug=True, host = "192.168.1.3", port = 5000,threaded=True) 
       
