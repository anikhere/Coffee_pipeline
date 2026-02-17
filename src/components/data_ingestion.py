from sklearn.model_selection import train_test_split
import sys
from logs.logger import get_logger
import sqlite3
import pandas as pd
from data.data_creation import load_coffee_data,export_sqlite_to_csv
from src.utils.utils import Read_Config
from src.constants.constants import *
import os 
from sklearn.model_selection import train_test_split
from src.config.config import Data_Ingestion_config
from src.config.artifacts import Data_Ingestion_Artifact
class DataIngestion:
    def __init__(self,config:Data_Ingestion_config):
        self.config = config
        self.logger = get_logger(__name__)
    def save_csv(self,csv_path,df):
        dirname = os.path.dirname(csv_path)
        os.makedirs(dirname,exist_ok=True)  
        df.to_csv(csv_path,index=False)
        self.logger.info('ok done check the directory updated')
    def split(self,df:pd.DataFrame):
        train_csv,test_csv = train_test_split(df,test_size=self.config.test_size,random_state=self.config.random_state)
        self.logger.info(f'the shape of train_csv is {train_csv.shape}')
        self.logger.info(f'the shape of train_csv is {test_csv.shape}')
        self.save_csv(self.config.train_file_path,train_csv)
        self.save_csv(self.config.test_file_path,test_csv)


        
    def initate_ingestion(self)->Data_Ingestion_Artifact:
        df = load_coffee_data(DB_PATH)
        print(df.head(5))
        self.logger.info(f'done with the df')
        self.save_csv(csv_path=self.config.raw_data_file,df=df)
        self.logger.info(f'ok done with the raw file')
        self.split(df=df)
        self.logger.info(f'and now done with the both csv s')
        data_ingestion_artifact= Data_Ingestion_Artifact(
            raw_file_path=self.config.raw_data_file,
            train_file_path=self.config.train_file_path,
            test_file_path=self.config.test_file_path
        )
        return data_ingestion_artifact


        
        


    
    