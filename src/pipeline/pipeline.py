from src.components.data_ingestion import DataIngestion
from src.config.config import *
from src.constants.constants import *
from src.config.artifacts import *
from src.utils.utils import *
from src.components.data_validation import Data_validation
from src.components.data_transformation import DataTransformation
from src.components.trainer import Model_trainer
from src.components.model_pusher import Pusher
import sys
import os 
from logs.logger import get_logger
import os
import boto3
from dataclasses import dataclass


logger = get_logger(__name__)


class Training_pipeline:
    def __init__(self):
        self.train_config = training_pipeline_config()
        self.logger = get_logger(__name__)

    
    def start_data_ingestion(self):
        self.data_ingest_config = Data_Ingestion_config(train_pipe=self.train_config)
        self.logger.info('ingestion_config_created')
        data_ingestion = DataIngestion(config=self.data_ingest_config)
        self.logger.info('starting the ingestion')
        self.data_ingest_artifact = data_ingestion.initate_ingestion()
        self.logger.info('completed ingestion')
        return self.data_ingest_artifact
    
    def start_validation(self,di_artifact):
        di_artifact = di_artifact
        self.logger.info('starting validation and config done ')
        self.dv_config = Data_val_config(train_pipe=self.train_config)
        validate = Data_validation(self.dv_config,di_artifact)
        val_artifact = validate.initiate_data_validation()
        self.logger.info('validation completed')
        return val_artifact
    
    def start_transformation(self,dv_artifact):
        dv_artifact = dv_artifact
        self.logger.info('starting the transformation')
        dt_config = Data_transformation_config(train_pipe=self.train_config)
        transformer = DataTransformation(dt_config,dv_artifact)
        trans_artifact = transformer.initate_data_transformation()
        self.logger.info('completed the transformation process')
        return trans_artifact
    
    def start_training(self,dt_artifact):
        dt_artifact = dt_artifact
        trainer_conifg = Model_trainer_config(train_pipe=self.train_config)
        self.logger.info('starting training')
        trained = Model_trainer(trainer_conifg,dt_artifact)
        trained_artifact = trained.initate_training()
        self.logger.info('of course done with training.....')
        return trained_artifact
    
    def run_pipe(self):
        try:
            di_artifact = self.start_data_ingestion()
            dv_artifact = self.start_validation(di_artifact)
            dt_artifact = self.start_transformation(dv_artifact)
            trainer_artifact= self.start_training(dt_artifact)
        except Exception as e:
            raise e


