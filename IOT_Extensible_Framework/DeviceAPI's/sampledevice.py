#This is the pseudo device

from flask import Flask,jsonify
import os
app = Flask(__name__)

@app.route('/inventory')
def inventory():
    invent = {
        "Brand": "BIOTRONIC",
        "Longevity": "5 years",
        "Weight": "21.5 grams",
        "Size": "4.57*4.45*0.75 cm",
        "Voltage": "2.8 V",
        "Average Projected Capacity" : "1.28 Ah"
        }
   
    return jsonify(invent)
   

@app.route('/monitor')
def monitor():
    monitor = {
         "Status": "Active",
         "Last Active":"23-02-2020",
         "Packet Error Rate": "3%",
         "Sensitivity ": "-123dB"
    }
    return jsonify(monitor)
    
if __name__ == '__main__':
    app.run()
