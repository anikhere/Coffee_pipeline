from src.components.data_ingestion import DataIngestion
from src.constants.constants import *
from src.config.config import training_pipeline_config,Data_Ingestion_config


if __name__ == "__main__":
    train_pipe = training_pipeline_config()
    di = Data_Ingestion_config(train_pipe=train_pipe)
    ingestion = DataIngestion(di)
    data_ingestion_artifact = ingestion.initate_ingestion()