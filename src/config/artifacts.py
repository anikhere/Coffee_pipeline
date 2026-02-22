# in a separate artifacts.py file
from dataclasses import dataclass

@dataclass
class Data_Ingestion_Artifact:
    raw_file_path: str
    train_file_path: str
    test_file_path: str

@dataclass
class Data_Val_artifact:
    validation_status:str
    valid_train_file:str
    valid_test_file:str
    invalid_train_file:str
    invalid_test_file:str
    report_file:str

@dataclass
class Data_Transformation_artifact:
    transformed_train_file:str
    transformed_test_file:str
    preprocessor_file_path:str
    model_file_path:str