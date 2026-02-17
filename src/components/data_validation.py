from exceptions.exception import CoffeepipelineException
from logs.logger import get_logger
import pandas as pd
import sys 
from utils.utils import Read_Config
from constants.constants import *
import os
class DataValidation:
    def __init__(self,csv_path:str):
        self.csv_path = csv_path
        self.logger= get_logger(self.__class__.__name__)
        config_yaml = Read_Config(CONFIG_FILE_PATH)
        self.train_data_path = config_yaml['data']['trained_file_path']
    @staticmethod
    def read_csv(csv_path:str)->pd.DataFrame:
        try:
            df = pd.read_csv(csv_path)
            return df
        except Exception as e:
            raise CoffeepipelineException(e,sys)
    def Validate_cols(self,df:pd.DataFrame):
        self.logger.info('Starting to check for columns')
        lenght = len(df.columns)
        if lenght == 