FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY main.py .

# Cache the model inside the docker image for faster loading when the app scales to zero.
RUN python -c "import torch; from torchvision.models import EfficientNet_V2_S_Weights; model = torch.hub.load('pytorch/vision:v0.18.0', 'efficientnet_v2_s', weights=EfficientNet_V2_S_Weights.DEFAULT); torch.save(model, '/app/efficientnet_v2_s.pth')"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]