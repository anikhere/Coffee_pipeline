from datetime import datetime
import os 
from src.utils.utils import Read_Config
from src.constants.constants import *

class training_pipeline_config:
    def __init__(self,timestamp = datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.yaml_file = Read_Config(CONFIG_FILE_PATH)
        self.pipeline_name = PIPE_NAME
        self.artifact_dir = os.path.join(self.yaml_file['paths']['artifact_dir'],f"{PIPE_NAME}__{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        self.timestamp: str=timestamp
        self.model= os.path.join(FINAL_MODEL_NAME)

class Data_Ingestion_config:
    def __init__(self,train_pipe:training_pipeline_config):
        self.data_ingestion_dir = os.path.join(train_pipe.artifact_dir,DATA_INGESTION_DIR)
        self.raw_dir = os.path.join(self.data_ingestion_dir,RAW_DATA_DIR)
        self.raw_data_file= os.path.join(self.data_ingestion_dir,RAW_DATA_DIR,RAW_DATA_FILE)
        self.processed_dir = os.path.join(self.data_ingestion_dir,PROCESSED_DATA_DIR)
        self.train_file_path = os.path.join(self.processed_dir,TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.processed_dir,TEST_FILE_NAME)
        self.test_size = TEST_SIZE
        self.random_state = RANDOM_STATE        

class Data_val_config:
    def __init__(self,train_pipe:training_pipeline_config):
        self.data_val_dir = os.path.join(train_pipe.artifact_dir,DATA_VALIDATION_DIR)
        self.data_valid_dir = os.path.join(self.data_val_dir,DATA_VALID_DIR)
        self.data_invalid_dir= os.path.join(self.data_val_dir,DATA_INVALID_DIR)
        self.data_report_dir = os.path.join(self.data_val_dir,DATA_REPORT_DIR)
        self.data_valid_train_file= os.path.join(self.data_valid_dir,TRAIN_FILE_NAME)
        self.data_valid_test_file = os.path.join(self.data_valid_dir,TEST_FILE_NAME)
        self.data_invalid_train_file = os.path.join(self.data_invalid_dir,TRAIN_FILE_NAME)
        self.data_invalid_test_file = os.path.join(self.data_invalid_dir,TEST_FILE_NAME)
        self.val_report_file = os.path.join(self.data_report_dir,DATA_REPORT_FILE)
        self.max_score = MAX_SCORE
        self.min_score = MIN_SCORE
        self.required_rows = MIN_ROWS_REQUIRED
        self.drift_threshold = DRIFT_THRESHOLD

class Data_transformation_config:
    def __init__(self,train_pipe:training_pipeline_config):
        self.train_pipe = train_pipe
        self.data_transform_dir= os.path.join(train_pipe.artifact_dir,TRANSFORMED_DIR)
        self.tranformed_file_dir = os.path.join(self.data_transform_dir,TRANSFORM_DIR)
        self.object_dir = os.path.join(self.data_transform_dir,OBJECT_DIR)
        self.model_dir = os.path.join(self.data_transform_dir,MODELS_DIR)
        self.transformed_train_path = os.path.join(self.tranformed_file_dir,TRAIN_FILE_NAME)
        self.transformed_test_path = os.path.join(self.tranformed_file_dir,TEST_FILE_NAME)
        self.preprocessor_file_path = os.path.join(self.object_dir,self.train_pipe.yaml_file['model']['pkl_file_name'])
        self.model_file_path = os.path.join(self.model_dir,self.train_pipe.yaml_file['model']['model_file_name'])
    
class Model_trainer_config:
    def __init__(self,train_pipe:training_pipeline_config):
        self.train_pipe = train_pipe
        self.trainer_dir = os.path.join(train_pipe.artifact_dir,TRAINER_DIR)
        self.model_dir = os.path.join(self.trainer_dir,MODEL_TRAINER_DIR)
        self.model_path = os.path.join(self.model_dir,TRANSFORMED_MODEL_NAME)
        self.cv = CV
        self.score = SCORE
        self.model_report_dir = os.path.join(self.trainer_dir,REPORT_DIR)
        self.model_report_file = os.path.join(self.model_report_dir,MODEL_REPORT_FILE)
        self.final_model_path = os.path.join(self.model_dir,FINAL_MODEL_NAME)
        os.makedirs(self.model_dir,exist_ok=True)
class Model_pusher_config:
    def __init__(self,train_pipe:training_pipeline_config):
        self.final_model_pkl = os.path.join(train_pipe.artifact_dir,PUSH_DIR,FINAL_MODEL_NAME)

        