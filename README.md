# Basic image classifier deployed on an Azure container app

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