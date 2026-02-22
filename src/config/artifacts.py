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