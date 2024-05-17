import os
import requests
import time


local_url = "http://localhost:8000/classify"
azure_functions_url = "https://testcontainerapp.mangodesert-a317eb57.westeurope.azurecontainerapps.io/classify"


# Index 270 -- white wolf, Arctic wolf, Canis lupus tundrarum
image_path = os.path.join("tests", "n02114548_white_wolf.jpg")
with open(image_path, "rb") as file:
    start_time = time.time()
    response = requests.post(azure_functions_url, files={"file": file})
    end_time = time.time()
duration = end_time - start_time
print(f"Time taken for the request: {duration:.2f} seconds")
print(response.json())

"""
When the instance has scaled down to zero - the first request takes 10.3 seconds -> This might also be due to downloading the model to disk first.
When the instance has scaled down to zero, and the model is cached in the docker image, the first request takes 7.6 seconds
When the instance is online, the request takes < 1 second (+- 0.7, 0.8 seconds)
"""
