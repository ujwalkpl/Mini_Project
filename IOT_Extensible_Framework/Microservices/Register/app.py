#Devices get registered here

from flask import Flask,request
from redis import Redis, RedisError,StrictRedis

redis = StrictRedis(host="redis-server",charset="utf-8", decode_responses=True,db=0)


app = Flask(__name__)
@app.route("/")
def hello():

    #name and id of the device is being passed to register the device more parameters could be provided
    name = request.args.get("name")
    id = request.args.get("id")
    if name!=None and id!=None:
        device = {}
        names = redis.mget(redis.keys())
        devices = list(zip(redis.keys(),names))
        try:
            redis.set(id,name)
            # visits = redis.incr("counter")
            
            print(redis.keys())
        except RedisError:
            html = "Error"
        html = "<h3>Device Registered!</h3> <br>\n" \
                "<b>Device Name:</b> {name} <b> Device Id: </b> {id} <br>\n" \
            "<b>Registered Devices:</b>{devices} \n"
        return html.format(devices=devices,name=name,id=id)
    return str("Provide Device name and id")

#This route clears the database
@app.route("/clear")
def clear():
    redis.flushdb()
    return "done"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)