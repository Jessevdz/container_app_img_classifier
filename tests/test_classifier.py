import os
import requests


local_url = "http://localhost:8000/classify"
azure_functions_url = "http://localhost/classify"


# Index 270 -- white wolf, Arctic wolf, Canis lupus tundrarum
image_path = os.path.join("tests", "n02114548_white_wolf.jpg")
with open(image_path, "rb") as file:
    response = requests.post(local_url, files={"file": file})
print(response.json())
