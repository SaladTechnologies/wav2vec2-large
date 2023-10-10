import torch
from fastapi import FastAPI, Request
from io import BytesIO
import os
from huggingsound import SpeechRecognitionModel
import uvicorn
import time


model_id = os.environ.get("MODEL_ID")
host = os.environ.get("HOST", "0.0.0.0")
port = int(os.environ.get("PORT", "1111"))

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SpeechRecognitionModel(model_id, device=device)

app = FastAPI()


@app.get("/hc")
async def health_check():
    return {"status": "ok"}


@app.post("/transcribe")
async def transcribe(request: Request):
    body: bytes = await request.body()
    audio = BytesIO(body)
    start = time.perf_counter()
    result = model.transcribe([audio])
    return {
        "text": result[0]["transcription"],
        "inference_time": time.perf_counter() - start,
    }


if __name__ == "__main__":
    print(f"Running {model_id} on {device}")
    uvicorn.run(app, host=host, port=port)
