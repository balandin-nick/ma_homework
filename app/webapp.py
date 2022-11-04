from typing import Any, Dict

from fastapi import FastAPI


app = FastAPI(
    title="Homework",
    description="Test FastApi application for Microservice Architecture",
)


@app.get("/")
def get_index() -> str:
    return "Hello!"


@app.get("/health")
def get_health() -> Dict[str, Any]:
    return {"status": "OK"}
