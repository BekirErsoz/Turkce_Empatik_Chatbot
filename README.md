# Türkçe Empatik Chatbot AI Servisi

Bu proje, Türkçe duygu analizi ve empatik yanıt üretimi yapan üretime hazır bir FastAPI mikro servisidir.

## Özellikler
* **Duygu Analizi** – `savasy/bert-base-turkish-sentiment-cased`
* **Yanıt Üretimi** – `bigscience/bloomz-560m` (Türkçe destekli, açık kaynak)
* Gradio veya mobil istemcilerin kolayca bağlanabileceği tek `/chat` uç noktası
* Docker ile dakikalar içinde dağıtım

## Hızlı Başlangıç

```bash
# Sanal ortam opsiyonel
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Swagger doküman: http://localhost:8000/docs

### Docker

```bash
docker build -t turkce-chatbot .
docker run -d -p 8000:8000 turkce-chatbot
```

## API Örneği

```bash
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message":"Bugün kendimi yalnız hissediyorum."}'
```

Yanıt

```json
{
  "reply": "...",
  "sentiment": {
    "label": "NEGATIVE",
    "score": 0.93
  }
}
```

## Lisans
Apache 2.0
