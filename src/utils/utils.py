import yaml
import os 
import numpy as np
import pickle
def Read_Config(config_path):
    with open(config_path) as file:
        config = yaml.safe_load(file)
    return config

def save_csv(self,csv_path,df):
    dirname = os.path.dirname(csv_path)
    os.makedirs(dirname,exist_ok=True)  
    df.to_csv(csv_path,index=False)

def write_yaml(file_path:str, data:dict):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path,'wb') as file:
            yaml.dump(data,file)
    except Exception as e:
        print(f"Error writing YAML file: {e}")

def save_object(file_path:str,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj,file)
    except Exception as e:
        print(f'the error is {e}')

def load_object(file_path:str):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'rb') as file:
            return pickle.load(file=file)
    except Exception as e:
        print(f'the error could be {e}')

def load_numpy(file_path:str):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'rb') as file:
            return np.load(file)
    except Exception as e:
        print(f'the error could be {e}')
def save_numpy(file_path:str,array):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file:
            np.save(file,array)
    except Exception as e:
        print(f'the error could be {e}')
         