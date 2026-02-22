from sklearn.model_selection import train_test_split
import sys
from logs.logger import get_logger
import sqlite3
import pandas as pd
from data.data_creation import load_coffee_data,export_sqlite_to_csv
from src.utils.utils import Read_Config,save_csv,write_yaml
from src.constants.constants import *
import os 
from sklearn.model_selection import train_test_split
from src.config.config import Data_Ingestion_config,Data_val_config
from src.config.artifacts import Data_Ingestion_Artifact,Data_Val_artifact
from scipy.stats import ks_2samp


class Data_validation:
    def __init__(self,data_ingest:Data_Ingestion_Artifact,train_config:Data_val_config):
        self.data_ingest = data_ingest
        self.train_config = train_config
        self.yaml_file = Read_Config(CONFIG_FILE_PATH)
        self.get_logger = get_logger(__name__)
        self.train_df = self.Load_csv(self.data_ingest.train_file_path)
        self.test_df= self.Load_csv(self.data_ingest.test_file_path)
    
    def Load_csv(self,csv_path):
        df = pd.read_csv(csv_path)
        if 'id' in df.columns:
            df = df.drop('id',axis=1)
        return df 
    
    def Check_rows(self,df:pd.DataFrame)->bool:
        self.get_logger.info(f'checking the minimum cols required')
        if df.shape[0] > self.train_config.required_rows:
            self.get_logger.info(f'ok you are above the min requirement')
            return True
        else:
            self.get_logger.info(f'please submit another csv')
            return False
        
    def check_cols(self,df)->bool:
        config_cols = set(self.yaml_file['columns'])
        expected_cols = set(df.columns)
        if expected_cols == config_cols:
            self.get_logger.info(f'the columns expected are {config_cols} and the actual columns are {expected_cols} and they match')
            mising_cols = config_cols - expected_cols
            extra_cols = expected_cols - config_cols
            if mising_cols:
                self.get_logger.info(f'missing columns: {mising_cols}')
            if extra_cols:
                self.get_logger.info(f'extra columns: {extra_cols}')
            return True
        else:
            self.get_logger.info(f'the columns expected are {config_cols} and the actual columns are {expected_cols} and they do not match')
            return False
        
    def validate_value_ranges(self, df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        
        # Get feature columns only (not target)
        feature_cols = FEATURE_COLUMNS
        
        # Create mask: True if all features in row are within range
        mask = (df[feature_cols] >= self.train_config.min_score).all(axis=1) & \
               (df[feature_cols] <= self.train_config.max_score).all(axis=1)
        
        # Split into valid and invalid
        valid_df = df[mask]
        invalid_df = df[~mask]
        
        # Log results
        self.get_logger.info(f"Value range validation: {len(valid_df)} valid, {len(invalid_df)} invalid rows")
        
        return valid_df, invalid_df
    
    def Null_check(self,df:pd.DataFrame):
        null = df.isna().sum().sum()
        if null > self.yaml_file['minimum_nulls']:
            mask = df.isna().any(axis=1)
            valid_csv = df[~mask]
            invalid_csv = df[mask]
        else:
            valid_csv = df
            invalid_csv = pd.DataFrame()
            print(f'no nulls were found so')
        return valid_csv,invalid_csv   
    
    def Data_drift(self,train_df,test_df,threshold):
        drift_report= {}
        for col in train_df.columns:
            train_data = train_df[col]
            test_data = test_df[col]
            pvalue = ks_2samp(train_data, test_data).pvalue
            if pvalue > threshold:
                drift_report[col] = 'No Drift'
            else:
                drift_report[col] = 'Drift Detected'
        os.makedirs(self.train_config.data_report_dir, exist_ok=True)
        write_yaml(self.train_config.val_report_file,drift_report)
        return drift_report


               
    def initiate_data_validation(self) -> Data_Val_artifact:
     try:
        self.get_logger.info("Starting data validation...")
        
        # STEP 1: Basic checks (raise error if fail)
        if not self.Check_rows(self.train_df):
            raise Exception('Train data does not meet minimum row requirements')
        if not self.Check_rows(self.test_df):
            raise Exception('Test data does not meet minimum row requirements')
        
        self.get_logger.info(" Row count checks passed")
        
        if not self.check_cols(self.train_df):
            raise Exception('Train data columns do not match expected configuration')
        if not self.check_cols(self.test_df):
            raise Exception('Test data columns do not match expected configuration')
        
        self.get_logger.info(" Column checks passed")
        
        # STEP 2: Validate TRAIN data (chain checks)
        valid_train, invalid_values_train = self.validate_value_ranges(self.train_df)
        valid_train, invalid_nulls_train = self.Null_check(valid_train)
        
        # Combine all invalid train rows
        all_invalid_train = pd.concat(
            [invalid_values_train, invalid_nulls_train],
            ignore_index=True
        )
        
        # STEP 3: Validate TEST data (same process)
        valid_test, invalid_values_test = self.validate_value_ranges(self.test_df)
        valid_test, invalid_nulls_test = self.Null_check(valid_test)
        
        all_invalid_test = pd.concat(
            [invalid_values_test, invalid_nulls_test],
            ignore_index=True
        )
        
        self.get_logger.info(f"Train: {len(valid_train)} valid, {len(all_invalid_train)} invalid")
        self.get_logger.info(f"Test: {len(valid_test)} valid, {len(all_invalid_test)} invalid")
        
        # STEP 4: Data drift detection
        drift_report = self.Data_drift(self.train_df,self.test_df,self.train_config.drift_threshold)  # hint: train, test, threshold
        self.get_logger.info("Drift detection completed")
        
        # STEP 5: Create directories
        os.makedirs(self.train_config.data_valid_dir, exist_ok=True)
        os.makedirs(self.train_config.data_invalid_dir, exist_ok=True)
        
        # STEP 6: Save validated data
        valid_train.to_csv(self.train_config.data_valid_train_file, index=False)
        all_invalid_train.to_csv(self.train_config.data_invalid_train_file, index=False)
        
        valid_test.to_csv(self.train_config.data_valid_test_file, index=False)  # hint: config path for valid test
        all_invalid_test.to_csv(self.train_config.data_invalid_test_file, index=False)  # hint: config path for invalid test
        
        self.get_logger.info(" All validated files saved")
        
        # STEP 7: Return artifact
        return Data_Val_artifact(
            validation_status=True,
            valid_train_file=self.train_config.data_valid_train_file,
            valid_test_file = self.train_config.data_valid_test_file,  # hint: from config
            invalid_train_file=self.train_config.data_invalid_train_file,
            invalid_test_file=self.train_config.data_invalid_test_file,
            report_file=self.train_config.val_report_file
        )
        
     except Exception as e:
        self.get_logger.error(f"Validation failed: {e}")
        raise e
    

