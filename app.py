from dotenv import load_dotenv
from src.pipeline.pipeline import Training_pipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response, RedirectResponse
from uvicorn import run as app_run
import pandas as pd

load_dotenv()  # load .env secrets

app = FastAPI()  # create the app

origins = ["*"]  # allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

@app.get('/', tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')

@app.get('/train')
async def train_route():
    try:
        train = Training_pipeline()
        train.run_pipe()
        return Response('training completed.....')
    except Exception as e:
        raise e 
    

if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8080)