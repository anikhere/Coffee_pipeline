# in a separate artifacts.py file
from dataclasses import dataclass

@dataclass
class Data_Ingestion_Artifact:
    raw_file_path: str
    train_file_path: str
    test_file_path: str