from fastapi import FastAPI
import fastapi_start.router_example

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}