

import yaml
def Read_Config(config_path):
    with open(config_path) as file:
        config = yaml.safe_load(file)
    return config

