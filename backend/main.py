from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from compiler import compile_app as run_compiler

app = FastAPI(title="AI App Compiler")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running",
        "status": "healthy"
    }


@app.post("/compile")
def compile_endpoint(request: PromptRequest):
    return run_compiler(request.prompt)