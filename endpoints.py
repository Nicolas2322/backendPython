from typing import Optional
from fastapi import FastAPI, status
from schemas.openai import OpenAISchema

app = FastAPI()

@app.post("/escucha_respuesta", status_code=status.HTTP_200_OK, tags=["OpenAI"])
def post_escucha(pregunta: OpenAISchema):
    return {"respuesta": pregunta.question}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
