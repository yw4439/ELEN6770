import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "Yanming Wei"}

@app.get("/uni/{uni_id}")
def read_item(uni_id: str = "yw4439", q: Union[str, None] = None):
    return {"uni_id": uni_id, "q": q}
