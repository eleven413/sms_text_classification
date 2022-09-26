import pickle
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/trained_spamclf_pipe_{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

preds_list = ["Not Spam", "SPAM!"]

def predict_pipeline(text):
    pred = model.predict([text])
    return preds_list[pred[0]]