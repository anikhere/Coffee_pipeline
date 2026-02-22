import yaml
import os 
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
        with open(file_path,'w') as file:
            yaml.dump(data,file)
    except Exception as e:
        print(f"Error writing YAML file: {e}")