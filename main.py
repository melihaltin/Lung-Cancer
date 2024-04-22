from src.Lung_Cancer.logging import logger

from Lung_Cancer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Lung_Cancer.pipeline.stage_02_data_validation import DataValidationPipeline
from Lung_Cancer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from Lung_Cancer.pipeline.stage_04_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
 
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


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataTransformationPipeline()
    pipeline.run()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    
    
    
STAGE_NAME = "Model Training stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = ModelTrainingPipeline()
    pipeline.run()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    