from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
# import uvicorn # for local testing

app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    pred: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    prediction = predict_pipeline(payload.text)
    return {"pred": prediction}

# for local testing
# if __name__ == "__main__":
#     uvicorn.run(app, host = "127.0.0.1", port = 8000)
#     # print(predict({"text":"hello this is a test"}))