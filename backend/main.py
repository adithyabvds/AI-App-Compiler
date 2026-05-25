from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI App Compiler")


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }


@app.post("/compile")
def compile_app(request: PromptRequest):

    return {
        "prompt": request.prompt,
        "status": "received"
    }