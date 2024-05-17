# Basic image classifier deployed on an Azure container app

## Timings
* When the instance has scaled down to zero, and the model is cached inside the docker image, the first request takes 7.6 seconds
* When the instance is online, the request takes < 1 second (+- 0.7, 0.8 seconds)

## Local testing
```
> cd app
> docker build -t test .
> docker run -p 8000:8000 --rm -it test
```

## Push a local docker image to Azure container registry
```
> az login
> az acr login --name <registry-name>
> docker tag <local-image>:<tag> <registry-name>.azurecr.io/<image-name>:<tag>
> docker push <registry-name>.azurecr.io/<image-name>:<tag>
```