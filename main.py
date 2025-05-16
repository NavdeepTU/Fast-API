from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello world"}

@app.get("/about")
def about():
    return {"message":"Campusx is a education platform where you can learn AI."}