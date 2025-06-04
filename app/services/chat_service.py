from app.models.sentiment import SentimentAnalyzer
from app.models.response import EmpathicResponder

_sentiment = SentimentAnalyzer()
_responder = EmpathicResponder()

def chat_process(text: str):
    sentiment = _sentiment(text)
    reply_text = _responder(text, sentiment['label'])
    return {"reply": reply_text, "sentiment": sentiment}
