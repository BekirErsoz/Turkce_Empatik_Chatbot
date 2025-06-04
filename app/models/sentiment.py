from transformers import pipeline
from loguru import logger

class SentimentAnalyzer:
    def __init__(self):
        logger.info("Loading Turkish sentiment model...")
        self.pipe = pipeline(
            "sentiment-analysis",
            model="savasy/bert-base-turkish-sentiment-cased",
            device=-1  # CPU; change to 0 for GPU
        )
        logger.info("Sentiment model loaded.")

    def __call__(self, text: str):
        result = self.pipe(text)[0]
        return {"label": result["label"], "score": float(result["score"])}
