import numpy as np
# constants.py
ARTIFACTS_DIR = 'artifacts'
# File paths (relative paths that don't change)
CONFIG_FILE_PATH = "src/config/config.yaml"
SCHEMA_FILE_PATH = "config/schema.yaml"
PIPE_NAME = 'Coffee_pipeline'
DB_PATH = "data/coffee.db"

# Database constants
DB_NAME = "coffee.db"
TABLE_NAME = "coffee_data"

# Column names (prevents typos!)
FEATURE_COLUMNS = [
    "acidity",
    "aroma", 
    "body",
    "flavor",
    "aftertaste",
    "balance"
]

TARGET_COLUMN = "quality"

# Model parameters
TEST_SIZE = 0.2
RANDOM_STATE = 42
MODEL_NAME = "coffee_model.pkl"

# Data validation thresholds
MIN_SCORE = 0.0
MAX_SCORE = 10.0
MIN_ROWS_REQUIRED = 30

# Artifact subdirectories
METRICS_DIR = "metrics"

# Log messages (optional but helpful)


# Quality labels
QUALITY_LABELS = {
    0: "Bad Quality",
    1: "Good Quality"
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##data_ingestion
DATA_INGESTION_DIR = "Data_ingestion"
RAW_DATA_DIR = "raw"
RAW_DATA_FILE = "coffee_data.csv"
PROCESSED_DATA_DIR = "Processed"
TEST_FILE_NAME = "test.csv"
TRAIN_FILE_NAME = "train.csv"
#=========================================================================================================
#data_validation
DATA_VALIDATION_DIR = "data_validation"
DATA_VALID_DIR = "valid"
DATA_INVALID_DIR = "invalid"
DATA_REPORT_DIR = "reports"
DATA_REPORT_FILE = "report.yaml"
DRIFT_THRESHOLD = 0.05

#data_transformation===========================================================================
TRANSFORMED_DIR = "Transformed"
MODELS_DIR = "models"
TRANSFORM_DIR = "transformed"
OBJECT_DIR = "objects"

kNN_input_params: dict = {
    'missing_values': np.nan,
    'n_neighbors':3,
    'weights':'uniform'
}
#====================================================================================
TRAINER_DIR = "Trainer"
MODEL_TRAINER_DIR = 'model_trainer'
TRANSFORMED_MODEL_NAME = "Model.pkl"
CV = 5
SCORE = 0.6
REPORT_DIR = 'reports'
MODEL_REPORT_FILE = 'model_report.yaml' 
FINAL_MODEL_NAME = "final_model.pkl"