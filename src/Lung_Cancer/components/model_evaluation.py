
from pathlib import Path
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import numpy as np
from Lung_Cancer.utils.common import save_json
import joblib
from Lung_Cancer.entity.config_entity import ModelEvaluationConfig
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        accuracy = accuracy_score(actual, pred)
        recall = recall_score(actual, pred)
        precision = precision_score(actual, pred)
        f1 = f1_score(actual, pred)
        return accuracy, recall, precision, f1

    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        prediction = model.predict(test_x)

        accuracy, recall, precision, f1 = self.eval_metrics(test_y, prediction)

        scores = {
            "accuracy": accuracy,
            "recall": recall,
            "precision": precision,
            "f1": f1
        }
       
        save_json(path=Path(self.config.metric_file_name), data=scores)
