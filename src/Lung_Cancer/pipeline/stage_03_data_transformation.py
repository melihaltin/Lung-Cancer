from Lung_Cancer.config.configuration import ConfigurationManager
from Lung_Cancer.components.data_transformation import DataTransformation
from Lung_Cancer.logging import logger


class DataTransformationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        data_transformation_config = self.config.get_data_transformation_config()
        self.data_transformation = DataTransformation(data_transformation_config)

    def run(self):
        
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation_config = DataTransformation(data_transformation_config)
            data_transformation_config.run()
        except Exception as e:
            logger.error(e)
            
            
            
            
    
if __name__ == "__main__":
    try:
        logger.info("Running data transformation pipeline")
        pipeline = DataTransformationPipeline()
        pipeline.run()
        logger.info("Data transformation pipeline completed successfully")
    except Exception as e:
        logger.error("Data transformation pipeline failed")
        logger.error(e)
        raise e    