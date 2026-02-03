
import sys
from logs.logger import get_logger
import sqlite3
import pandas as pd
import yaml
from utils.utils import Read_Config
from constants.constants import *
import os 


class DataIngestion:
    def __init__(self,csv_path:str):
        self.csv_path = csv_path
        self.logger = get_logger(self.__class__.__name__)
        config_yaml = Read_Config(CONFIG_FILE_PATH)
        self.db_path = config_yaml['paths']['database_path']
        self.artifacts_dir= config_yaml['paths']['artifact_dir']
        self.artifacts_subdir = config_yaml['paths']['artifacts_sub']
    
    def ingest_data(self):
        try:
            self.logger.info(DATA_INGESTION_START)
            connection= sqlite3.connect(self.db_path)
            query = f'select * from {TABLE_NAME}'
            df = pd.read_sql_query(query,connection)
            os.makedirs(self.artifacts_dir,exist_ok=True)
            RAW_DATA_DIR_PATH = os.path.join(self.artifacts_dir,self.artifacts_subdir)
            os.makedirs(RAW_DATA_DIR_PATH,exist_ok=True)
            self.csv_path = os.path.join(RAW_DATA_DIR_PATH,os.path.basename(self.csv_path))
            if not os.path.exists(self.csv_path):
                df.to_csv(self.csv_path,index=False)
                self.logger.info(f"Data ingested and saved to {self.csv_path}")
            else:
                self.logger.info(f"CSV file already exists at {self.csv_path}. Skipping save.")
            self.logger.info(DATA_INGESTION_SUCCESS)
            connection.close()
            return df 
        except Exception as e:
            print(e)

di = DataIngestion(csv_path="artifacts/raw/data.csv")
di.ingest_data()



    
    