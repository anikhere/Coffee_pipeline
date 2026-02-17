from datetime import datetime
import os 
from src.utils.utils import Read_Config
from src.constants.constants import *

class training_pipeline_config:
    def __init__(self):
        self.yaml_file = Read_Config(CONFIG_FILE_PATH)
        self.pipeline_name = PIPE_NAME
        self.artifact_dir = os.path.join(self.yaml_file['paths']['artifact_dir'],f"{PIPE_NAME}__{datetime.now().strftime('%m%d%Y__%H%M%S')}"
)
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

        