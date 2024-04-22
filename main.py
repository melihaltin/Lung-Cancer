from src.Lung_Cancer.logging import logger

from src.Lung_Cancer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Lung_Cancer.pipeline.stage_02_data_validation import DataValidationPipeline


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
    
   
   
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e    
    