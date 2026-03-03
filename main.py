from src.components.data_ingestion import DataIngestion,Data_Ingestion_Artifact
from src.components.data_validation import Data_validation
from src.components.data_transformation import DataTransformation
from src.components.trainer import Model_trainer
from src.components.model_pusher import Pusher
from src.constants.constants import *
from src.config.config import training_pipeline_config,Model_pusher_config,Data_Ingestion_config,Model_trainer_config,Data_val_config,Data_transformation_config
from src.utils.utils import *
from src.config.artifacts import *
import pandas as pd



if __name__ == "__main__":
    train_pipe = training_pipeline_config()
    di = Data_Ingestion_config(train_pipe=train_pipe)
    ingestion = DataIngestion(di)
    data_ingestion_artifact = ingestion.initate_ingestion()
    dv = Data_validation(data_ingest=data_ingestion_artifact,train_config=Data_val_config(train_pipe=train_pipe))
    data_val_artifact = dv.initiate_data_validation()

    
   
    dt = DataTransformation(
    config=Data_transformation_config(train_pipe=train_pipe),
    dv = data_val_artifact
)
    data_trans_artifact = dt.initate_data_transformation()
    train_config = Model_trainer_config(train_pipe=training_pipeline_config())
    mt = Model_trainer(train_config=Model_trainer_config(train_pipe=train_pipe),dt_artifact=data_trans_artifact)
    model_artifact = mt.initate_training()
    push = Model_pusher_config(train_pipe=train_pipe)
    model_push = Pusher(push_config=push,train_config=train_config)
    model_push.Push_models()
