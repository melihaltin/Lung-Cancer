from src.Lung_Cancer.logging import logger
from src.Lung_Cancer.config.configuration import ConfigurationManager
from src.Lung_Cancer.components.data_ingestion import DataIngestion

        
class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.error(e)


STAGE_NAME = "Data Ingestion"
if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed")
        logger.error(e)
        raise e
    
           