from src.Lung_Cancer.logging import logger

from src.Lung_Cancer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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
    