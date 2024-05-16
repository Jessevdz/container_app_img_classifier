from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import torch
import torchvision.transforms as transforms
from torchvision.models import EfficientNet_V2_S_Weights

app = FastAPI()

model = torch.hub.load(
    "pytorch/vision:v0.18.0",
    "efficientnet_v2_s",
    weights=EfficientNet_V2_S_Weights.DEFAULT,
)
model.eval()

transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    input_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
    _, predicted = torch.max(output, 1)
    return {"class_index": predicted.item()}
