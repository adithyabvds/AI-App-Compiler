from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from compiler import compile_app as run_compiler

app = FastAPI(
    title="AI App Compiler"
)

# ----------------------------
# CORS Configuration
# ----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Request Schema
# ----------------------------

class PromptRequest(BaseModel):
    prompt: str


# ----------------------------
# Health Check
# ----------------------------

@app.get("/")
def home():

    return {
        "message": "AI App Compiler Running",
        "status": "healthy"
    }


# ----------------------------
# Compile Endpoint
# ----------------------------

@app.post("/compile")
def compile_endpoint(
    request: PromptRequest
):

    return run_compiler(
        request.prompt
    )