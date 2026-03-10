from dotenv import load_dotenv
from src.pipeline.pipeline import Training_pipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response, RedirectResponse
from uvicorn import run as app_run
import pandas as pd
from fastapi.templating import Jinja2Templates
from src.utils.utils import save_object,load_object
from src.utils.network_model import Network_model
from src.config.config import Model_trainer_config,training_pipeline_config,Data_transformation_config

trainer = Model_trainer_config(train_pipe=training_pipeline_config)
transformer = Data_transformation_config(train_pipe=training_pipeline_config)

load_dotenv()  # load .env secrets

app = FastAPI()  # create the app

origins = ["*"]  # allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

templates = Jinja2Templates(directory='templates')

@app.get('/')
async def index(request:Request):
    return templates.TemplateResponse('table.html',{'request':request})

@app.get('/train')
async def train_route():
    try:
        train = Training_pipeline()
        train.run_pipe()
        return Response('training completed.....')
    except Exception as e:
        raise e 
@app.post('/predict')
async def predict_route(request:Request,file:UploadFile=File(...)):
    df = pd.read_csv(file.file)
    model = load_object(trainer.final_model_path)
    preprocessor = load_object(transformer.preprocessor_file_path)
    main_model = Network_model(model=model,preprocessor=preprocessor)
    pred = main_model.predict(df)
    df.to_csv('pred_output/output.csv')
    print(pred)
    df['Predictions'] = pred
    return {'predictions': pred.tolist()}
    


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8080)