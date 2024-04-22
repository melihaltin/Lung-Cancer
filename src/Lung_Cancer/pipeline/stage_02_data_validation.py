

from src.Lung_Cancer.logging import logger
from src.Lung_Cancer.config.configuration import ConfigurationManager
from src.Lung_Cancer.components.data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
    
    
    
STAGE_NAME = "DATA VALIDATION"    
if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}")
        pipeline = DataValidationPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed")
        logger.error(e)
        raise e    