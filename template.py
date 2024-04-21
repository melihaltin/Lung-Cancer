import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO , format='[%(asctime)s]- %(name)s - %(levelname)s - %(message)s')

# Project name
PROJECT_NAME = 'Lung_Cancer'

list_of_files = [
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",

    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",    
]


for file in list_of_files:
    filepath = Path(file)
    filedir , filename = os.path.split(filepath)

    if filedir!= "" and not os.path.exists(filedir):
        logging.info(f"Creating directory {filedir}")
        os.makedirs(filedir)
    if not os.path.exists(filepath):
        logging.info(f"Creating file {filepath}")
        with open(filepath, "w") as f:
            f.write("")
    else:
        logging.info(f"File {filepath} already exists")        

logging.info("Project structure created successfully")    






