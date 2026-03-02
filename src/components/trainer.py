from src.config.config import training_pipeline_config,Data_transformation_config,Model_trainer_config
from src.config.artifacts import Model_train_artifact,Data_Transformation_artifact,Classification_metrics
from src.utils.utils import save_object,load_object,Read_Config,load_numpy,save_numpy,write_yaml
from src.utils.model import trainer
from src.utils.network_model import Network_model
import os 
from src.constants.constants import *
from sklearn.linear_model import LogisticRegression
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
        self.X_test = self.test_df[:,:-1]
        self.y_test = self.test_df[:,-1]
        self.logger.info("started the training of the model")
        report,best_model,yaml_dict = trainer(self.X_train,self.y_train,self.models,self.params,min_score=SCORE,X_test=self.X_test,y_test=self.y_test)
        write_yaml(file_path=self.train_config.model_report_file,data=yaml_dict)
        best_model_name = max(report, key=lambda x: report[x]['test_score'].f1)
        save_object(self.train_config.model_path,best_model)
        self.logger.info(f"model training completed and the best model is {best_model_name} with f1 score {report[best_model_name]['test_score'].f1}")
        preprocessor = load_object(self.dt_artifact.preprocessor_file_path)
        main_model = Network_model(model=best_model,preprocessor=preprocessor)
        save_object(self.train_config.final_model_path,main_model)
        Model_artifact = Model_train_artifact(
            model_path=self.train_config.final_model_path,
            best_model=best_model_name,
            train_score=report[best_model_name]['train_score'],
            test_score=report[best_model_name]['test_score'],
            preprocessor_path=self.dt_artifact.preprocessor_file_path
        )
        return Model_artifact


