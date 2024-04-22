from Lung_Cancer.config.configuration import ConfigurationManager
from Lung_Cancer.components.model_training import ModelTrainer
from Lung_Cancer.logging import logger

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def run(self):
        
        try:
            config_manager = ConfigurationManager()
            config = config_manager
            model_trainer = ModelTrainer(config)
            model = model_trainer.train()
            model_path = model_trainer.save_model(model)
            print('Model trained successfully and saved at ', model_path)
            
        except Exception as e:
            print('Training failed')
            print(e)
            
        
        

if __name__ == "__main__":
    try:
        logger.info("Running model training pipeline")
        pipeline = ModelTrainingPipeline()
        pipeline.run()
        logger.info("Model training pipeline completed successfully")
    except Exception as e :
        logger.error("Model training pipeline failed")
        logger.error(e)
        raise e    
