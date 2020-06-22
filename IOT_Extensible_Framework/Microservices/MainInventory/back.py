from flask import Flask,jsonify,request
import time
import requests

#background task will be running here
#This will fetch the inventory by calling the api passed
def background_task(URL):
    # delay = 2
    print('Task running')
    r = requests.get(url = URL) 
    # print(f'Simulating {delay} second delay')
    # time.sleep(delay)

    print(len(URL))
    print("Task complete")
    return (r.json())
