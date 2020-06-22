from flask import Flask,jsonify
import requests
import time
import json
from redis import Redis, RedisError,StrictRedis
from rq import Queue
from rq import use_connection
from back import background_task
from rq.job import Job

#connection to redis database, database is chose to be 0
redis = StrictRedis(host="redis-server",charset="utf-8", decode_responses=True,db=0)

#connection to redis database, database is chose to be 1
r = StrictRedis(host='redis-server',db=1)

#initialise the queue for managing asynchronous task 
q = Queue(connection=r)

app = Flask(__name__)

@app.route('/')
def hello():
    all_data = {}

    #This will hold all the device names
    device = redis.mget(redis.keys())

    #This will hold all the device ids
    keys = redis.keys()
    
    print(keys)
    all_jobs = []
    for key,dev in zip(keys,device):
        URL = "http://inventory:5001?id=" + str(dev)

        #This inventory will be fetched in the background
        job = q.enqueue(background_task,URL)
        
        all_jobs.append(job.id)

    check=1
    full_jobs = Job.fetch_many(all_jobs,connection=r)
   
    while check:
        check=0
        for job in full_jobs:
            if str(job.get_status()).lower()!="finished":
                check=1
                break
        
    for key,job in zip(keys,full_jobs):
        result = job.result
        all_data.update({key:result})
    print("fetching inventory")
  
    return jsonify(all_data)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010,debug=True)
