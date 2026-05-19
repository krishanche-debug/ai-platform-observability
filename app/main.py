import time

from fastapi import FastAPI
from pydantic import BaseModel

from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response

from langchain_ollama import OllamaLLM

# FastAPI app
app = FastAPI()

# Load local LLM
llm = OllamaLLM(model="gemma4:26b")

# Prometheus metrics
REQUEST_COUNT = Counter(
    "llm_requests_total",
    "Total LLM requests"
)

REQUEST_LATENCY = Histogram(
    "llm_request_latency_seconds",
    "LLM request latency"
)

# Request body
class PromptRequest(BaseModel):
    prompt: str

# AI inference endpoint
@app.post("/generate")
def generate(request: PromptRequest):

    REQUEST_COUNT.inc()

    start_time = time.time()

    response = llm.invoke(request.prompt)

    REQUEST_LATENCY.observe(time.time() - start_time)

    return {
        "response": response
    }

# Metrics endpoint
@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type="text/plain"
    )