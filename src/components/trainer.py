from src.config.config import training_pipeline_config,Data_transformation_config,Model_trainer_config
from src.config.artifacts import Model_train_artifact,Data_Transformation_artifact,classification_metrics
from src.utils.utils import save_object,load_object,Read_Config,load_numpy,save_numpy
import os 
from src.constants.constants import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier,RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from logs.logger import get_logger
class Model_trainer:
    def __init__(self,train_config:Model_trainer_config,dt_artifact:Data_Transformation_artifact):
        self.train_config = train_config
        self.dt_artifact = dt_artifact
        self.logger = get_logger(__name__)
        self.yaml_file = Read_Config(SCHEMA_FILE_PATH)
        self.models = {
            'random_forest': RandomForestClassifier(),
            'logistic_regression': LogisticRegression(),
            'knn': KNeighborsClassifier(),
            'decision_tree': DecisionTreeClassifier(),
            'adaboost': AdaBoostClassifier(),
            'gradient_boosting': GradientBoostingClassifier()
        }
        self.params = {
            'random_forest': {
                'n_estimators': [100, 200],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5]
            },
            'logistic_regression': {
                'C': [0.1, 1, 10],
                'solver': ['liblinear']
            },
            'knn': {
                'n_neighbors': [3, 5, 7],
                'weights': ['uniform', 'distance']
            },
            'decision_tree': {
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5]
            },
            'adaboost': {
                'n_estimators': [50, 100],
                'learning_rate': [0.01, 0.1]
            },
            'gradient_boosting': {
                'n_estimators': [100, 200],
                'learning_rate': [0.01, 0.1],
                'max_depth': [3, 5]
            }
        }
    
    def initate_training(self):
        self.train_df = load_numpy(self.dt_artifact.transformed_train_file)
        self.test_df = load_numpy(self.dt_artifact.transformed_test_file)
        self.X_train = self.train_df[:,:-1]
        self.y_train = self.train_df[:,-1]
        self.X_test= self.test_df[:,:-1]
        self.y_test = self.test_df[:,-1]