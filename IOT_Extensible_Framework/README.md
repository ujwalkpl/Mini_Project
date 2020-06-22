# IOT_EXTENSIBLE_FRAMEWORK
A service provider for IOT which provides plug-n-play architecture where new support and features can be added on the fly without changing the framework.

## 🔧 Instructions to run

### Run Docker on swarm mode either Online(https://labs.play-with-docker.com/) or in your local computer

### Create a overlay network 

```
docker network create --driver overlay --attachable my-net
```

### Clone, build and run the visualiser code
```
git clone https://github.com/dockersamples/docker-swarm-visualizer

cd docker-swarm-visualizer
docker-compose up -d


docker service create \
  --name=viz \
  --publish=8080:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  dockersamples/visualizer
```


### Clone and run all the basic services
```
git clone https://github.com/ujwalkpl/IOT_EXTENSIBLE_FRAMEWORK.git

cd docker-image/flask

docker stack deploy --compose-file docker-compose.yml App
 
```


Visualize the services on the port  ```8080```
Register your devices using the ```5005```
Get inventory of all the devices on the port ```5010```
Get inventory of the required device on the port ```5001``` <br>

#### Suppose docker is running on ```192.168.99.100```
Then to register a new device run ```192.168.99.100:5005?id=121&name=sensor1``` <br>
where sensor1 is the name of the device and 121 is the device id



## Additional docker commands

### To create a new service 
Follow the same code and change the url of the service inside the Maininventory file so that that particular instance will be called

### To scale up a service 

Change the App_inventory to the name of the service to be scaled
```
docker service scale App_inventory=5
```


### To update a service

Change the name ```App_inventory``` to the name of the service to be updated and provide the image name and the version required
```
docker service update --image ujwalkpl/inventory:1.0.0 App_inventory
```





 
