from src.components.data_ingestion import DataIngestion,Data_Ingestion_Artifact
from src.components.data_validation import Data_validation
from src.constants.constants import *
from src.config.config import training_pipeline_config,Data_Ingestion_config,Data_val_config
from src.utils.utils import Read_Config,save_csv,write_yaml
import pandas as pd



if __name__ == "__main__":
    train_pipe = training_pipeline_config()
    di = Data_Ingestion_config(train_pipe=train_pipe)
    ingestion = DataIngestion(di)
    data_ingestion_artifact = ingestion.initate_ingestion()
    dv = Data_validation(data_ingest=data_ingestion_artifact,train_config=Data_val_config(train_pipe=train_pipe))
    data_val_artifact = dv.initiate_data_validation()