from fastapi import FastAPI
from pydantic import BaseModel
from bedrock_client import extract_entities

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Entity Extraction API!"
    }

@app.post("/extract")
def extract(request: TextRequest):
    result = extract_entities(request.text)
    return {
        "entities": result
    }