import os 
import urllib.request as request
import zipfile
from src.Lung_Cancer.logging import logger
from src.Lung_Cancer.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config:DataIngestionConfig) :
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading data from {self.config.data_source}")
            request.urlretrieve(self.config.data_source, self.config.local_data_file)
            logger.info(f"Downloaded data to {self.config.local_data_file}")
        else:
            logger.info(f"Data already exists at {self.config.local_data_file}")    
            
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)