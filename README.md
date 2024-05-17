# Basic image classifier deployed on an Azure container app

## Push a local docker image to Azure container registry
```
> az login
> az acr login --name <registry-name>
> docker tag <local-image>:<tag> <registry-name>.azurecr.io/<image-name>:<tag>
> docker push <registry-name>.azurecr.io/<image-name>:<tag>
```