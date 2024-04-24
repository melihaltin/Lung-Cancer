
from Lung_Cancer.config.configuration import ConfigurationManager
from Lung_Cancer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def run(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.save_results()
        except Exception as e:
            print(e)
            print("Model Evaluation failed")
            raise e

if __name__ == "__main__":
    try:
        pipeline = ModelEvaluationPipeline()
        pipeline.run()
    except Exception as e:
        print(e)
        print("Model Evaluation failed")
        raise e
    