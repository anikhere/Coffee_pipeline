# constants.py

# File paths (relative paths that don't change)
CONFIG_FILE_PATH = "config/config.yaml"
SCHEMA_FILE_PATH = "config/schema.yaml"

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
RAW_DATA_DIR = "raw"
PROCESSED_DATA_DIR = "processed"
MODELS_DIR = "models"
METRICS_DIR = "metrics"

# Log messages (optional but helpful)
DATA_INGESTION_START = "Data ingestion started"
DATA_INGESTION_SUCCESS = "Data ingestion completed successfully"
MODEL_TRAINING_START = "Model training started"
MODEL_TRAINING_SUCCESS = "Model training completed"

# Quality labels
QUALITY_LABELS = {
    0: "Bad Quality",
    1: "Good Quality"
}