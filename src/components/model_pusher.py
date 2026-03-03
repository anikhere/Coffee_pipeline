import os 
from src.constants.constants import *
from src.config.config import Model_pusher_config,Model_trainer_config
from src.config.artifacts import Model_pusher
from src.utils.utils import load_object,save_object
class Pusher:
    def __init__(self,push_config:Model_pusher_config,train_config:Model_trainer_config):
        self.pusher = push_config
        self.train = train_config
    def Push_models(self)-> Model_pusher:
        os.makedirs(os.path.dirname(self.pusher.final_model_pkl), exist_ok=True)
        model = load_object(self.train.final_model_path)
        save_object(self.pusher.final_model_pkl,obj=model)
        pusher_artifact = Model_pusher(
            final_model=self.pusher.final_model_pkl
        )
        return pusher_artifact


    