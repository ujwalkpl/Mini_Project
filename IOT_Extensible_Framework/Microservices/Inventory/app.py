from flask import Flask,jsonify,request
import requests
import time
import os
import redis



app = Flask(__name__)

@app.route('/')
def hello():
    # name = os.environ.get('MYAPP_NAME', 'MyApp')
    # print(name)
    id = request.args.get("id")
    
    URL = "http://trustify.pythonanywhere.com/inventory"
    r = requests.get(url = URL) 
    print("inventory")
    # extracting data in json format 
    data = r.json() 
    data.update({"id":id})
    print("fetching inventory")
    
    return jsonify(data)
    # return '<br\><h3><center>Hello, Welcome to Dockerized Flask (' + name + ') !!!<center></h3>'

if __name__ == '__main__':
    port = int(os.environ.get('MYAPP_PORT', 5001))

    app.run(host='0.0.0.0', port=port)
