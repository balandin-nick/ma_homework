from typing import Any, Dict

from fastapi import FastAPI


app = FastAPI(
    title="Homework 1",
    description="Test FastApi application for Microservice Architecture",
)


@app.get("/health")
def hello_world() -> Dict[str, Any]:
    return {"status": "OK"}
