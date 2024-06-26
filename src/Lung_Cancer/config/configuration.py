from src.Lung_Cancer.constants import *  # noqa: F403
from src.Lung_Cancer.utils.common import read_yaml , create_directories
from src.Lung_Cancer.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainingConfig


class ConfigurationManager:
    
    def __init__(
        self, 
        config_file_path = CONFIG_FILE_PATH,  
        params_file_path = PARAMS_FILE_PATH,
        schema_file_path = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            data_source=config.data_source,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS + self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config    
    
    def get_data_transformation_config(self):
        self.config = self.config.data_transformation
        
        create_directories([self.config.root_dir])
        config = DataTransformationConfig(
            root_dir = Path(self.config.root_dir),
            data_file = Path(self.config.data_file),
            transformed_data_file = Path(self.config.transformed_data_file)
        )
        return config
    
    
    def get_model_training_config(self):
        self.config = self.config.model_training
        
        create_directories([self.config.root_dir])
        return ModelTrainingConfig(
            root_dir = Path(self.config.root_dir),
            train_data = Path(self.config.train_data),
        )
        
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            metric_file_name = config.metric_file_name,
            target_column = "LUNG_CANCER"
           
        )

        return model_evaluation_config