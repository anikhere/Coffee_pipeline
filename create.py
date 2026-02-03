## going to build the whole pipeline structure
import os 
files = [
    'components/__init__.py',
    'utils/__init__.py',
    'config/__init__.py',
    'constants/__init__.py',
    'data/__init__.py',
    'logs/logger.py',
    'main.py',
    'pipeline/pipeline.py',
    'docker/Dockerfile',
    'docker/.dockerignore',
]


]
def create_dir(path):
    for file in path:
        dir_path = os.path.dirname(file)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path,exist_ok=True)
            print(f'created Directory: {dir_path}')
        
        if not os.path.exists(file):
            with open(file,'w') as f:
                f.write(f'#this is{file} ')
            print('created file')

create_dir(files)
