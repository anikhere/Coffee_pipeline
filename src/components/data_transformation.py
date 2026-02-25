from sklearn.model_selection import train_test_split
import sys
from logs.logger import get_logger
import pandas as pd
from src.utils.utils import Read_Config,save_csv,save_object,load_object,save_numpy,load_numpy
from src.constants.constants import *
import numpy as np
import os 
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from src.config.config import Data_Ingestion_config,Data_transformation_config
from src.config.artifacts import Data_Ingestion_Artifact,Data_Transformation_artifact,Data_Val_artifact
class DataTransformation:
        def __init__(self,config:Data_transformation_config,dv:Data_Val_artifact):
            self.config = config
            self.dv = dv
            self.logger = get_logger(__name__)
            self.logger.info("Data Transformation class initialized")
            self.yaml_file = Read_Config(CONFIG_FILE_PATH)
            self.train_df = pd.read_csv(self.dv.valid_train_file)
            self.test_df = pd.read_csv(self.dv.valid_test_file)
        
        def get_transform_pipeline(self):
            self.logger.info("Creating transformation pipeline")
            KNN = KNNImputer(**kNN_input_params)
            scaler = StandardScaler()
            pipe = Pipeline(steps=[
                ('imputer',KNN),
                ('scaler',scaler)
            ])
            return pipe
        
        def initate_data_transformation(self)->Data_Transformation_artifact:
            self.pipe = self.get_transform_pipeline()
            input_feature = self.train_df.drop(TARGET_COLUMN,axis=1)
            output_feature = self.train_df[TARGET_COLUMN]
            self.transformed_train_input = self.pipe.fit_transform(input_feature)
            self.transformed_test_input = self.pipe.transform(self.test_df.drop(TARGET_COLUMN,axis=1))
            self.transformed_train_output = output_feature.values
            train_arr = np.c_[self.transformed_train_input,self.transformed_train_output]
            test_arr = np.c_[self.transformed_test_input,self.test_df[TARGET_COLUMN].values]
            save_numpy(self.config.transformed_train_path,train_arr)
            save_numpy(self.config.transformed_test_path,test_arr)
            save_object(self.config.preprocessor_file_path,self.pipe)
            self.logger.info("Data transformation completed successfully")
            Data_artitfact = Data_Transformation_artifact(
                transformed_train_file=self.config.transformed_train_path,
                transformed_test_file=self.config.transformed_test_path,
                preprocessor_file_path=self.config.preprocessor_file_path
            )



