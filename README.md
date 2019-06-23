# Run python container

This container depends on redis, make sure you are running redis before you run this container.

## 1. Run redis container

```
  docker run -d --name=redis redis:latest
  
```

## 2. Run this container
Pass container name or ip address of redis

```
  docker run -it -p 8080:5000 -e "redis_host=redis" kammana/nodeapp:0.0.1 
```

## 3. If you are running on local machine

Open browser and put the following url
http://localhost:8080
