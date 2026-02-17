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

MODELS_DIR = "models"
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